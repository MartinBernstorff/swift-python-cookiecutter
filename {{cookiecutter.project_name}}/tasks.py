"""
This project uses Invoke (pyinvoke.org) for task management.
Install it via:

```
pip install invoke
```

And then run:

```
inv --list
```

If you do not wish to use invoke you can simply delete this file.
"""


import platform
import re
from pathlib import Path
from typing import Optional

from invoke import Context, Result, task

NOT_WINDOWS = platform.system() != "Windows"


def echo_header(msg: str):
    print(f"\n--- {msg} ---")

class MsgType:
    
    @property
    def is_windows(self):
        return platform.system() == "Windows"
    
    @property
    def DOING(self):
        return "DOING:" if self.is_windows else b'\xf0\x9f\xa4\x96'.decode()

    @property
    def GOOD(self):
        return "DONE:" if self.is_windows else b'\xe2\x9c\x85'.decode()
    
    @property
    def FAIL(self):
        return "FAILED:" if self.is_windows else b'\xf0\x9f\x9a\xa8'.decode()
    
    @property
    def WARN(self):
        return "WARNING:" if self.is_windows else b'\xf0\x9f\x9a\xa7'.decode()
    
    @property
    def SYNC(self):
        return "SYNCING:" if self.is_windows else b'\xf0\x9f\x9a\x82'.decode()
    
    @property
    def PY(self):
        return "" if self.is_windows else b'\xf0\x9f\x90\x8d'.decode()
    
    @property
    def CLEAN(self):
        return "CLEANING:" if self.is_windows else b'\xf0\x9f\xa7\xb9'.decode()
    
    @property
    def TEST(self):
        return "TESTING:" if self.is_windows else b'\xf0\x9f\xa7\xaa'.decode()
    
    @property
    def COMMUNICATE(self):
        return "COMMUNICATING:" if self.is_windows else b'\xf0\x9f\x93\xa3'.decode()
    
    @property
    def EXAMINE(self):
        return "VIEWING:" if self.is_windows else b'\xf0\x9f\x94\x8d'.decode()

msg_type = MsgType()


def git_init(c: Context, branch: str = "main"):
    """Initialize a git repository if it does not exist yet."""
    # If no .git directory exits
    if not Path(".git").exists():
        echo_header(f"{msg_type.DOING} Initializing Git repository")
        c.run(f"git init -b {branch}")
        c.run("git add .")
        c.run("git commit -m 'Init'")
        print(f"{msg_type.GOOD} Git repository initialized")
    else:
        print(f"{msg_type.GOOD} Git repository already initialized")


def setup_venv(
    c: Context,
    python: str,
    venv_name : Optional[str] = None,
) -> str:
    """Create a virtual environment if it does not exist yet.
    
    Args:
        c: The invoke context.
        python: The python executable to use.
        venv_name: The name of the virtual environment. Defaults to ".venv".
    """
    if venv_name is None:
        venv_name = ".venv"

    if not Path(venv_name).exists():
        echo_header(
            f"{msg_type.DOING} Creating virtual environment using {msg_type.PY}:{python}",
        )
        c.run(f"{python} -m venv {venv_name}")
        print(f"{msg_type.GOOD} Virtual environment created")
    else:
        print(f"{msg_type.GOOD} Virtual environment already exists")
    return venv_name


def _add_commit(c: Context, msg: Optional[str] = None):
    print(f"{msg_type.DOING} Adding and committing changes")
    c.run("git add .")

    if msg is None:
        msg = input("Commit message: ")

    c.run(f'git commit -m "{msg}"', pty=NOT_WINDOWS, hide=True)
    print(f"{msg_type.GOOD} Changes added and committed")


def is_uncommitted_changes(c: Context) -> bool:
    git_status_result: Result = c.run(
        "git status --porcelain",
        pty=NOT_WINDOWS,
        hide=True,
    )

    uncommitted_changes = git_status_result.stdout != ""
    return uncommitted_changes


def add_and_commit(c: Context, msg: Optional[str] = None):
    """Add and commit all changes."""
    if is_uncommitted_changes(c):
        uncommitted_changes_descr = c.run(
            "git status --porcelain",
            pty=NOT_WINDOWS,
            hide=True,
        ).stdout

        echo_header(
            f"{msg_type.WARN} Uncommitted changes detected",
        )

        for line in uncommitted_changes_descr.splitlines():
            print(f"    {line.strip()}")
        print("\n")
        _add_commit(c, msg=msg)


def branch_exists_on_remote(c: Context) -> bool:
    branch_name = Path(".git/HEAD").read_text().split("/")[-1].strip()

    branch_exists_result: Result = c.run(
        f"git ls-remote --heads origin {branch_name}",
        hide=True,
    )

    return branch_name in branch_exists_result.stdout


def update_branch(c: Context):
    echo_header(f"{msg_type.SYNC} Syncing branch with remote")

    if not branch_exists_on_remote(c):
        c.run("git push --set-upstream origin HEAD")
    else:
        print("Pulling")
        c.run("git pull")
        print("Pushing")
        c.run("git push")


def create_pr(c: Context):
    c.run(
        "gh pr create --web",
        pty=NOT_WINDOWS,
    )


def update_pr(c: Context):
    echo_header(f"{msg_type.COMMUNICATE} Syncing PR")
    # Get current branch name
    branch_name = Path(".git/HEAD").read_text().split("/")[-1].strip()
    pr_result: Result = c.run(
        "gh pr list --state OPEN",
        pty=False,
        hide=True,
    )

    if branch_name not in pr_result.stdout:
        create_pr(c)
    else:
        open_web = input("Open in browser? [y/n] ")
        if "y" in open_web.lower():
            c.run("gh pr view --web", pty=NOT_WINDOWS)


def exit_if_remaining_errors(result: Result):
    # Find N remaining using regex

    if "error" in result.stdout:
        errors_remaining = re.findall(r"\d+(?=( remaining))", result.stdout)[0]
        if errors_remaining != "0":
            exit(1)


def pre_commit(c: Context, auto_fix: bool):
    """Run pre-commit checks."""

    # Essential to have a clean working directory before pre-commit to avoid committing
    # heterogenous files under a "style: linting" commit
    if is_uncommitted_changes(c):
        print(
            f"{msg_type.WARN} Your git working directory is not clean. Stash or commit before running pre-commit.",
        )
        exit(1)

    echo_header(f"{msg_type.CLEAN} Running pre-commit checks")
    pre_commit_cmd = "pre-commit run --all-files"
    result = c.run(pre_commit_cmd, pty=NOT_WINDOWS, warn=True)

    exit_if_remaining_errors(result)

    if ("fixed" in result.stdout or "reformatted" in result.stdout) and auto_fix:
        _add_commit(c, msg="style: Auto-fixes from pre-commit")

        print(f"{msg_type.DOING} Fixed errors, re-running pre-commit checks")
        second_result = c.run(pre_commit_cmd, pty=NOT_WINDOWS, warn=True)
        exit_if_remaining_errors(second_result)
    else:
        if result.return_code != 0:
            print(f"{msg_type.FAIL} Pre-commit checks failed")
            exit(1)


@task
def static_type_checks(c: Context):
    echo_header(f"{msg_type.CLEAN} Running static type checks")
    c.run("pyright .", pty=NOT_WINDOWS)


@task
def install(c: Context, pip_args: str = "", msg: bool = True):
    """Install the project in editable mode using pip install"""
    if msg:
        echo_header(f"{msg_type.DOING} Installing project")

    if NOT_WINDOWS:
        c.run(f"pip install -e '.[dev,tests,docs]' {pip_args}")
    else:
        c.run(f"pip install -e .[dev,tests,docs] {pip_args}")


@task
def setup(c: Context, python: str = "python3.9"):
    """Confirm that a git repo exists and setup a virtual environment.
    
    Args:
        python: Path to the python executable to use for the virtual environment.
    """
    git_init(c)

    venv_name = setup_venv(c, python=python)

    if venv_name is not None:
        print(
            f"{msg_type.DOING} Activate your virtual environment by running: \n\n\t\t source {venv_name}/bin/activate \n",
        )
        print(
            f"{msg_type.DOING} Then install the project by running: \n\n\t\t inv install\n",
        )


@task
def update(c: Context):
    """Update dependencies."""
    echo_header(f"{msg_type.DOING} Updating project")
    install(c, pip_args="--upgrade", msg=False)


@task
def test(c: Context):
    """Run tests"""
    echo_header(f"{msg_type.TEST} Running tests")
    test_result: Result = c.run(
        "pytest tests/ -n auto -rfE --failed-first -p no:cov --disable-warnings -q",
        warn=True,
        pty=NOT_WINDOWS,
    )

    # If "failed" in the pytest results
    if "failed" in test_result.stdout:
        print("\n\n\n")
        echo_header("Failed tests")

        # Get lines with "FAILED" in them from the .pytest_results file
        failed_tests = [
            line for line in test_result.stdout if line.startswith("FAILED")
        ]

        for line in failed_tests:
            # Remove from start of line until /test_
            line_sans_prefix = line[line.find("test_") :]

            # Keep only that after ::
            line_sans_suffix = line_sans_prefix[line_sans_prefix.find("::") + 2 :]
            print(f"FAILED {msg_type.FAIL} #{line_sans_suffix}     ")

    if test_result.return_code != 0:
        exit(0)


def test_for_rej():
    # Get all paths in current directory or subdirectories that end in .rej
    rej_files = list(Path(".").rglob("*.rej"))

    if len(rej_files) > 0:
        print(f"\n{msg_type.FAIL} Found .rej files leftover from cruft update.\n")
        for file in rej_files:
            print(f"    /{file}")
        print("\nResolve the conflicts and try again. \n")
        exit(1)


@task
def lint(c: Context, auto_fix: bool = False):
    """Lint the project using the pre-commit hooks and mypy."""
    test_for_rej()
    pre_commit(c=c, auto_fix=auto_fix)
    static_type_checks(c)


@task
def pr(c: Context, auto_fix: bool = False):
    """Run all checks and update the PR."""
    add_and_commit(c)
    lint(c, auto_fix=auto_fix)
    test(c)
    update_branch(c)
    update_pr(c)


@task
def docs(c: Context, view: bool = False, view_only: bool = False):
    """
    Build and view docs. If neither build or view are specified, both are run.
    """
    if not view_only:
        echo_header(f"{msg_type.DOING}: Building docs")
        c.run("sphinx-build -b html docs docs/_build/html")
    if view or view_only:
        echo_header(f"{msg_type.EXAMINE}: Opening docs in browser")
        # check the OS and open the docs in the browser
        if NOT_WINDOWS:
            c.run("open docs/_build/html/index.html")
        else:
            c.run("start docs/_build/html/index.html")
