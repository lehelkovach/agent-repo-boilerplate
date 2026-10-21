from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "apply_template.py"
VALIDATOR = ROOT / "scripts" / "validate_template.py"


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )


def snapshot(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        result[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


class InstallerTests(unittest.TestCase):
    def install(self, target: Path, apply: bool = True) -> subprocess.CompletedProcess[str]:
        args = [sys.executable, str(INSTALLER), str(target)]
        if apply:
            args.append("--apply")
        return run(*args)

    def test_dry_run_is_default(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "sample"
            target.mkdir()
            result = self.install(target, apply=False)
            self.assertIn("DRY-RUN WRITE", result.stdout)
            self.assertFalse((target / "AGENTS.md").exists())

    def test_fresh_install_is_idempotent_and_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "sample"
            target.mkdir()
            self.install(target)
            first = snapshot(target)
            second_result = self.install(target)
            second = snapshot(target)
            self.assertEqual(first, second)
            self.assertIn("No changes required.", second_result.stdout)
            run(sys.executable, str(VALIDATOR), str(target))

    def test_existing_agents_file_is_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "sample"
            target.mkdir()
            custom = "# Existing policy\n\nKeep this exact instruction.\n"
            (target / "AGENTS.md").write_text(custom, encoding="utf-8")
            result = self.install(target)
            self.assertEqual(custom, (target / "AGENTS.md").read_text(encoding="utf-8"))
            self.assertIn("PRESERVE", result.stdout)
            self.assertTrue((target / ".AGENT/RUNBOOK.md").is_file())

    def test_existing_symlink_is_not_followed_or_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "sample"
            target.mkdir()
            external = root / "external-agents.md"
            custom = "# External policy\n"
            external.write_text(custom, encoding="utf-8")
            (target / "AGENTS.md").symlink_to(external)

            result = self.install(target)

            self.assertEqual(custom, external.read_text(encoding="utf-8"))
            self.assertTrue((target / "AGENTS.md").is_symlink())
            self.assertIn("PRESERVE", result.stdout)

    def test_v1_instructions_and_log_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "legacy"
            legacy = target / ".AGENT"
            legacy.mkdir(parents=True)
            agent = (
                "# Legacy agent\n\n## Base-Agent Section\n\nGeneric.\n\n"
                "#### Below: Repository-Specific Directions\n\n"
                "Never alter the public API without approval.\n"
            )
            log = "# Agent Action Log\n\nHistorical evidence.\n"
            (legacy / "agent.md").write_text(agent, encoding="utf-8")
            (legacy / "agent-action-log.md").write_text(log, encoding="utf-8")

            self.install(target)

            agents = (target / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("Never alter the public API without approval.", agents)
            self.assertEqual(
                log,
                (legacy / "archive/v1/agent-action-log.md").read_text(encoding="utf-8"),
            )
            self.assertEqual(agent, (legacy / "agent.md").read_text(encoding="utf-8"))

    def test_reports_directory_is_installed_and_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "sample"
            target.mkdir()
            self.install(target)
            readme = target / ".AGENT/reports/README.md"
            self.assertTrue(readme.is_file())
            content = readme.read_text(encoding="utf-8")
            self.assertIn("YYYY-MM-DD-<slug>.md", content)
            self.assertIn("## Index", content)
            for name in ("AGENTS.md", ".AGENT/RUNBOOK.md", ".cursor/rules/agent-conventions.mdc"):
                self.assertIn(".AGENT/reports/", (target / name).read_text(encoding="utf-8"))

            readme.unlink()
            result = subprocess.run(
                [sys.executable, str(VALIDATOR), str(target)],
                text=True,
                capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("missing required file: .AGENT/reports/README.md", result.stdout)

    def test_task_specific_handoffs_merge_from_two_worktrees(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory) / "repository"
            repository.mkdir()
            run("git", "init", "-b", "main", cwd=repository)
            run("git", "config", "user.email", "tests@example.invalid", cwd=repository)
            run("git", "config", "user.name", "Boilerplate Tests", cwd=repository)
            self.install(repository)
            run("git", "add", ".", cwd=repository)
            run("git", "commit", "-m", "Install boilerplate", cwd=repository)

            first = Path(directory) / "task-one"
            second = Path(directory) / "task-two"
            run("git", "worktree", "add", "-b", "agent/task-one", str(first), cwd=repository)
            run("git", "worktree", "add", "-b", "agent/task-two", str(second), cwd=repository)

            handoff_one = first / ".AGENT/handoffs/101-first.md"
            handoff_two = second / ".AGENT/handoffs/102-second.md"
            handoff_one.write_text("# Handoff 101\n", encoding="utf-8")
            handoff_two.write_text("# Handoff 102\n", encoding="utf-8")
            run("git", "add", str(handoff_one.relative_to(first)), cwd=first)
            run("git", "commit", "-m", "Add task 101 handoff", cwd=first)
            run("git", "add", str(handoff_two.relative_to(second)), cwd=second)
            run("git", "commit", "-m", "Add task 102 handoff", cwd=second)

            run("git", "merge", "--no-edit", "agent/task-one", cwd=repository)
            run("git", "merge", "--no-edit", "agent/task-two", cwd=repository)
            self.assertTrue((repository / ".AGENT/handoffs/101-first.md").is_file())
            self.assertTrue((repository / ".AGENT/handoffs/102-second.md").is_file())


if __name__ == "__main__":
    unittest.main()
