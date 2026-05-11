#!/usr/bin/env python3
"""Minimal aidev repository validator.

The checker intentionally validates durable workflow contracts, not arbitrary
business code. It is safe to run in local development and GitHub Actions.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ALLOWED_TASK_STATUSES = {
    "draft",
    "proposed",
    "approved",
    "in_progress",
    "blocked",
    "in_review",
    "completed",
    "superseded",
    "example",
}

ALLOWED_STEP_STATUSES = {
    "pending",
    "planned",
    "in_progress",
    "blocked",
    "completed",
    "skipped",
    "not_applicable",
    "n/a",
}

ACTIVE_TASK_STATUSES = {"approved", "in_progress", "blocked", "in_review"}
CLOSED_TASK_STATUSES = {"completed"}
GIT_WORKFLOW_MODES = {"simple", "feature_branch", "parallel_ai"}

REQUIRED_FILES = [
    "AIDEV_MANIFEST.md",
    "PROJECT_RULES.md",
    "CORE/AI_WORKFLOW.md",
    "CORE/TASK_TEMPLATE.md",
    "CORE/REVIEW_RULES.md",
    "CORE/INDEX_REGISTRY.md",
    "CORE/GIT_WORKFLOW.md",
    "PROJECT/PROJECT_PROFILE.md",
    "PROJECT/PROJECT_RULES.md",
    "PROJECT/GIT_WORKFLOW.md",
    "PROJECT/FEATURE_MAP.md",
    "PROJECT/FILE_MAP.md",
    "PROJECT/IMPLEMENTATION_MAP.md",
    "PROJECT/API_ROUTE_MAP.md",
    "PROJECT/FUNCTION_SIGNATURE_INDEX.md",
    "PROJECT/DTO_CONTRACT_INDEX.md",
    "PROJECT/PERMISSION_INDEX.md",
    "PROJECT/STATE_MACHINE_INDEX.md",
    "PROJECT/TEST_VERIFICATION_MATRIX.md",
    "PROJECT/TRACEABILITY_MATRIX.md",
    "PROJECT/DECISION_LOG.md",
    "PROJECT/RISK_REGISTER.md",
    "TASKS",
]

REQUIRED_INDEX_FILES = [
    "PROJECT/FEATURE_MAP.md",
    "PROJECT/FILE_MAP.md",
    "PROJECT/IMPLEMENTATION_MAP.md",
    "PROJECT/API_ROUTE_MAP.md",
    "PROJECT/FUNCTION_SIGNATURE_INDEX.md",
    "PROJECT/DTO_CONTRACT_INDEX.md",
    "PROJECT/PERMISSION_INDEX.md",
    "PROJECT/STATE_MACHINE_INDEX.md",
    "PROJECT/TEST_VERIFICATION_MATRIX.md",
    "PROJECT/ADMIN_FRONTEND_MAP.md",
    "PROJECT/CONFIG_ENV_INDEX.md",
    "PROJECT/TRACEABILITY_MATRIX.md",
    "PROJECT/DECISION_LOG.md",
    "PROJECT/RISK_REGISTER.md",
]

BASIC_TASK_SECTIONS = {
    "goal",
    "non-goals",
    "implementation steps",
    "index updates",
    "verification gates",
}

ACTIVE_TASK_SECTIONS = {
    "goal",
    "non-goals",
    "business context",
    "dependencies",
    "affected areas",
    "write scope",
    "git workflow",
    "implementation steps",
    "index updates",
    "verification gates",
    "review plan",
}

COMPLETED_TASK_SECTIONS = {
    "completion evidence",
}

EXAMPLE_TASK_SECTIONS = {
    "goal",
    "non-goals",
    "business context",
    "mode history",
    "dependencies",
    "assumptions and open questions",
    "affected areas",
    "write scope",
    "git workflow",
    "implementation steps",
    "data model changes",
    "api changes",
    "function and data contract changes",
    "integration changes",
    "security requirements",
    "observability requirements",
    "index updates",
    "verification gates",
    "rollback / compensation",
    "review plan",
    "learning / extension impact",
    "completion evidence",
}


@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    message: str


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_heading(text: str) -> str:
    cleaned = text.strip().lower()
    cleaned = re.sub(r"^\d+[a-z]?\.\s+", "", cleaned)
    return cleaned


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def collect_headings(text: str) -> set[str]:
    headings: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^##+\s+(.+?)\s*$", line)
        if match:
            headings.add(normalize_heading(match.group(1)))
    return headings


def extract_section(text: str, heading_name: str) -> str:
    target = normalize_heading(heading_name)
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        match = re.match(r"^##+\s+(.+?)\s*$", line)
        if match and normalize_heading(match.group(1)) == target:
            start = index + 1
            break
    if start is None:
        return ""
    end = len(lines)
    for index in range(start, len(lines)):
        if re.match(r"^##+\s+.+?\s*$", lines[index]):
            end = index
            break
    return "\n".join(lines[start:end]).strip()


def extract_status(text: str) -> str | None:
    for line in text.splitlines()[:40]:
        match = re.match(r"^Status:\s*(.+?)\s*$", line, flags=re.IGNORECASE)
        if match:
            return match.group(1).strip().lower()
    return None


def extract_task_step_statuses(text: str) -> list[str]:
    statuses: list[str] = []
    section = extract_section(text, "Implementation Steps")
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip().lower() for cell in stripped.strip("|").split("|")]
        if len(cells) < 2 or cells[0] in {"step id", "step"}:
            continue
        statuses.append(cells[1])
    return statuses


def has_unchecked_box(text: str) -> bool:
    return bool(re.search(r"(?m)^\s*[-*]\s+\[\s\]\s+", text))


def section_has_real_content(section: str) -> bool:
    cleaned = [
        line.strip()
        for line in section.splitlines()
        if line.strip() and not line.strip().startswith("```")
    ]
    placeholders = {"-", "- <path>", "<path>", "<command or review gate>"}
    return any(line not in placeholders for line in cleaned)


def run_git(root: Path, args: list[str]) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def check_required_files(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for item in REQUIRED_FILES:
        path = root / item
        if not path.exists():
            findings.append(Finding("ERROR", item, "required aidev file or directory is missing"))
        elif path.is_file() and path.stat().st_size == 0:
            findings.append(Finding("ERROR", item, "required aidev file is empty"))
    return findings


def check_index_files(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for item in REQUIRED_INDEX_FILES:
        path = root / item
        if not path.exists():
            findings.append(Finding("ERROR", item, "required project index is missing"))
            continue
        text = read_text(path)
        if "TODO" in text:
            findings.append(Finding("WARN", item, "index contains TODO marker"))
        if len(text.strip()) < 80:
            findings.append(Finding("ERROR", item, "index is too sparse to be useful"))
    return findings


def check_task_file(path: Path, root: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = read_text(path)
    rel = relative(path, root)
    status = extract_status(text)
    headings = collect_headings(text)

    if status is None:
        findings.append(Finding("ERROR", rel, "missing top-level Status field"))
        return findings

    if status not in ALLOWED_TASK_STATUSES:
        allowed = ", ".join(sorted(ALLOWED_TASK_STATUSES))
        findings.append(Finding("ERROR", rel, f"invalid Status '{status}', expected one of: {allowed}"))
        return findings

    required = set(BASIC_TASK_SECTIONS)
    if status in ACTIVE_TASK_STATUSES:
        required |= ACTIVE_TASK_SECTIONS
    if status in CLOSED_TASK_STATUSES:
        required |= COMPLETED_TASK_SECTIONS
    if status == "example":
        required |= EXAMPLE_TASK_SECTIONS

    missing = sorted(required - headings)
    for section in missing:
        findings.append(Finding("ERROR", rel, f"missing required task section: {section}"))

    if status in CLOSED_TASK_STATUSES and "review plan" not in headings:
        findings.append(Finding("ERROR", rel, "completed task must include Review Plan"))

    if status in CLOSED_TASK_STATUSES and has_unchecked_box(text):
        findings.append(Finding("ERROR", rel, "completed task still has unchecked checklist items"))

    if status in CLOSED_TASK_STATUSES:
        forbidden_statuses = {"pending", "planned", "in_progress", "blocked"}
        for step_status in extract_task_step_statuses(text):
            if step_status not in ALLOWED_STEP_STATUSES:
                findings.append(Finding("ERROR", rel, f"invalid step status '{step_status}'"))
            elif step_status in forbidden_statuses:
                findings.append(Finding("ERROR", rel, f"completed task has unfinished step status '{step_status}'"))
    else:
        for step_status in extract_task_step_statuses(text):
            if step_status not in ALLOWED_STEP_STATUSES:
                findings.append(Finding("ERROR", rel, f"invalid step status '{step_status}'"))

    for section in ("Index Updates", "Verification Gates"):
        if section.lower() in headings and not section_has_real_content(extract_section(text, section)):
            findings.append(Finding("ERROR", rel, f"{section} section is empty or placeholder-only"))

    return findings


def check_tasks(root: Path) -> list[Finding]:
    tasks_dir = root / "TASKS"
    findings: list[Finding] = []
    task_files = sorted(tasks_dir.glob("*.md")) if tasks_dir.exists() else []
    if not task_files:
        return [Finding("ERROR", "TASKS", "no task files found")]
    for task_file in task_files:
        findings.extend(check_task_file(task_file, root))
    return findings


def check_git_workflow(root: Path) -> list[Finding]:
    path = root / "PROJECT/GIT_WORKFLOW.md"
    findings: list[Finding] = []
    if not path.exists():
        return [Finding("ERROR", "PROJECT/GIT_WORKFLOW.md", "missing project Git workflow file")]

    text = read_text(path)
    match = re.search(r"git_workflow_mode:\s*([a-z_]+)", text)
    if not match:
        findings.append(Finding("ERROR", "PROJECT/GIT_WORKFLOW.md", "missing git_workflow_mode value"))
        return findings

    mode = match.group(1)
    if mode not in GIT_WORKFLOW_MODES:
        allowed = ", ".join(sorted(GIT_WORKFLOW_MODES))
        findings.append(Finding("ERROR", "PROJECT/GIT_WORKFLOW.md", f"invalid git_workflow_mode '{mode}', expected one of: {allowed}"))
        return findings

    branch = run_git(root, ["rev-parse", "--abbrev-ref", "HEAD"])
    if mode in {"feature_branch", "parallel_ai"} and branch in {"main", "master"}:
        findings.append(Finding("ERROR", "PROJECT/GIT_WORKFLOW.md", f"mode '{mode}' does not allow Build work directly on {branch}"))

    return findings


def check_source_index_sync(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    source_roots = [root / "Sources", root / "Tests"]
    source_files: list[Path] = []
    for source_root in source_roots:
        if source_root.exists():
            source_files.extend(
                path
                for path in source_root.rglob("*")
                if path.is_file() and ".build" not in path.parts
            )

    if not source_files:
        return findings

    file_map = read_text(root / "PROJECT/FILE_MAP.md") if (root / "PROJECT/FILE_MAP.md").exists() else ""
    implementation_map = (
        read_text(root / "PROJECT/IMPLEMENTATION_MAP.md")
        if (root / "PROJECT/IMPLEMENTATION_MAP.md").exists()
        else ""
    )

    for source_file in source_files:
        rel = relative(source_file, root)
        if rel not in file_map:
            findings.append(Finding("ERROR", "PROJECT/FILE_MAP.md", f"missing source file entry: {rel}"))
        if rel not in implementation_map:
            findings.append(Finding("ERROR", "PROJECT/IMPLEMENTATION_MAP.md", f"missing implementation map entry: {rel}"))

    return findings


def format_findings(findings: Iterable[Finding]) -> tuple[int, str]:
    findings_list = list(findings)
    errors = [finding for finding in findings_list if finding.severity == "ERROR"]
    warnings = [finding for finding in findings_list if finding.severity == "WARN"]

    lines: list[str] = []
    if not findings_list:
        lines.append("aidev check passed")
        return 0, "\n".join(lines)

    for finding in errors + warnings:
        lines.append(f"{finding.severity}: {finding.path}: {finding.message}")

    lines.append("")
    lines.append(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s)")
    return (1 if errors else 0), "\n".join(lines)


def run_check(root: Path) -> int:
    findings: list[Finding] = []
    findings.extend(check_required_files(root))
    findings.extend(check_index_files(root))
    findings.extend(check_tasks(root))
    findings.extend(check_git_workflow(root))
    findings.extend(check_source_index_sync(root))

    exit_code, output = format_findings(findings)
    print(output)
    return exit_code


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="aidev", description="AI_DEV workflow helper")
    parser.add_argument("command", choices=["check"], help="command to run")
    parser.add_argument(
        "--root",
        type=Path,
        default=repo_root_from_script(),
        help="path to the ai_dev root directory",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if args.command == "check":
        return run_check(root)
    return 1


if __name__ == "__main__":
    sys.exit(main())
