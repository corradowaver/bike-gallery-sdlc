"""PRE-SETUP-001-R1-R5: check Git behavior in disposable isolated storage."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


# PRE-SETUP-001-R1: environment exceptions and common local files.
CASES = {
    "PRE-SETUP-001-R1": {
        True: [
            ".env", "frontend/.env.local", "backend/.env.test",
            ".idea/workspace.xml", "frontend/.vscode/settings.json",
            "backend/service.iml", "frontend/.DS_Store", "Thumbs.db",
            "backend/app.log",
        ],
        False: [".env.example", "frontend/.env.example", "backend/.env.example"],
    },
    # PRE-SETUP-001-R2: generated files and module boundaries.
    "PRE-SETUP-001-R2": {
        True: [
            "frontend/node_modules/vue/index.js", "frontend/dist/index.html",
            "frontend/coverage/lcov.info", "frontend/.vite/cache.json",
            "frontend/playwright-report/index.html",
            "frontend/test-results/result.txt", "frontend/tsconfig.app.tsbuildinfo",
        ],
        False: ["frontend/src/dist/example.ts", "docs/dist/example.md"],
    },
    # PRE-SETUP-001-R3: Maven output and root-anchored scope.
    "PRE-SETUP-001-R3": {
        True: [
            "backend/target/classes/example/App.class", "backend/target/app.jar",
            "backend/target/site/jacoco/jacoco.xml",
        ],
        False: ["backend/src/test/resources/target/sample.txt", "docs/target/example.md"],
    },
    # PRE-SETUP-001-R4: files needed to reproduce and maintain the project.
    "PRE-SETUP-001-R4": {
        False: [
            ".gitignore", "frontend/.gitignore", "backend/.gitignore",
            "frontend/package.json", "frontend/package-lock.json",
            "frontend/vite.config.ts", "frontend/src/App.vue", "backend/pom.xml",
            "backend/mvnw", "backend/mvnw.cmd",
            "backend/.mvn/wrapper/maven-wrapper.properties",
            "backend/.mvn/wrapper/maven-wrapper.jar",
            "backend/src/main/java/example/App.java",
            "backend/src/test/resources/photo.jpg", "compose.yaml", "Dockerfile",
            "AGENTS.md", "docs/quality.md", "docs/decisions/PRE-SETUP-001.md",
            "openspec/config.yaml",
        ],
    },
}


def find_project_root(script_path):
    """PRE-SETUP-001-R5: locate the project at active or archived change depth."""
    for candidate in Path(script_path).resolve().parents:
        if (candidate / "openspec/config.yaml").is_file() or (candidate / "openspec/config.yml").is_file():
            return candidate
    raise RuntimeError("Cannot locate project root: no ancestor OpenSpec configuration")


def verify():
    # PRE-SETUP-001-R5: never use the user's index or external Git configuration.
    git = shutil.which("git")
    if git is None:
        print("NOT RUN PRE-SETUP-001-R5: Git is unavailable")
        return 2

    project = find_project_root(__file__)
    env = {key: value for key, value in os.environ.items()
           if not key.upper().startswith("GIT_")}
    env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_SYSTEM=os.devnull,
               GIT_CONFIG_GLOBAL=os.devnull)

    temporary_parent = Path(tempfile.gettempdir()).resolve()
    with tempfile.TemporaryDirectory(prefix="pre-setup-001-", dir=temporary_parent) as name:
        temporary = Path(name).resolve()
        # Verify the resolved cleanup target before TemporaryDirectory removes it.
        if temporary.parent != temporary_parent or not temporary.name.startswith("pre-setup-001-"):
            raise RuntimeError("Unexpected temporary directory location")
        repository = temporary / "repo"
        repository.mkdir()
        template = temporary / "empty-template"
        template.mkdir()
        excludes = temporary / "empty-excludes"
        excludes.touch()

        def run_git(*arguments, input_text=None):
            return subprocess.run(
                [git, "-c", f"core.excludesFile={excludes}", *arguments],
                cwd=repository, env=env, input=input_text,
                text=True, encoding="utf-8", capture_output=True, check=False,
            )

        initialized = run_git("init", "--quiet", f"--template={template}")
        if initialized.returncode != 0:
            raise RuntimeError(f"git init failed: {initialized.stderr}")
        info_exclude = repository / ".git/info/exclude"
        if info_exclude.exists() and any(
            line.strip() and not line.lstrip().startswith("#")
            for line in info_exclude.read_text().splitlines()
        ):
            raise RuntimeError("Unexpected repository exclude rules")

        for relative in (".gitignore", "frontend/.gitignore", "backend/.gitignore"):
            source = project / relative
            if not source.is_file():
                raise RuntimeError(f"Required ignore file missing: {relative}")
            destination = repository / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)

        failures = 0
        total = 0
        for requirement, expectations in CASES.items():
            for expected, paths in expectations.items():
                for path in paths:
                    # -z and --non-matching provide explicit records for negative cases.
                    result = run_git("check-ignore", "--no-index", "-v", "-z",
                                     "--non-matching", "--stdin", input_text=path + "\0")
                    if result.returncode not in (0, 1):
                        raise RuntimeError(f"git check-ignore failed: {result.stderr}")
                    fields = result.stdout.split("\0")
                    if len(fields) != 5 or fields[3] != path or fields[4] != "":
                        raise RuntimeError(f"Malformed Git output for {path}: {result.stdout!r}")
                    source, line, pattern = fields[:3]
                    ignored = bool(pattern) and not pattern.startswith("!")
                    passed = ignored == expected
                    failures += not passed
                    total += 1
                    rule = f"{source}:{line}:{pattern}" if pattern else "no matching rule"
                    print(f"{'PASS' if passed else 'FAIL'} {requirement} {path}: "
                          f"ignored={ignored}, expected={expected}; {rule}")
        print(f"{'FAIL' if failures else 'PASS'} PRE-SETUP-001-R5: "
              f"{total - failures}/{total} cases passed; isolated temporary repository")
        return 1 if failures else 0


if __name__ == "__main__":
    try:
        sys.exit(verify())
    except (OSError, RuntimeError) as error:
        print(f"FAIL PRE-SETUP-001-R5: {error}", file=sys.stderr)
        sys.exit(1)
