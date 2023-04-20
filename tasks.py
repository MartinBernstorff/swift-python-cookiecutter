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


import os
import shutil
from pathlib import Path

from invoke import Context, task

new_instance_dir = Path("swift-python")


@task
def setup_instance(c: Context):
    """Setup while instantiating the project."""
    shutil.rmtree(new_instance_dir)

    for invoke_command in ["setup", "install", "lint", "test", "docs"]:
        c.run(f"inv {invoke_command}")


@task
def cruft_create(c: Context):
    new_instance_dir.rmdir()

    if shutil.which("cruft") is None:
        c.run("pip install cruft")
    c.run("cruft create . -y")


@task
def test_instantiation(c: Context):
    """Test that the project can be instantiated."""
    cruft_create(c)
    setup_instance(c)


@task
def lint(c: Context):
    c.run("rm -f pyproject.toml")
    c.run("black .")

    # Copy the file from {\{\{cookiecutter.project_name\}\}}/pyproject.toml to pyproject.toml
    c.run(r"cp \{\{cookiecutter.project_name\}\}/pyproject.toml pyproject.toml")

    # Remove all lines starting with {% and ending with %}
    with Path("pyproject.toml").open("r") as f:
        content = f.read()
        content = "\n".join(
            [line for line in content.split("\n") if not line.startswith("{%")],
        )

        # Keep only stuffbetween [tool.ruff] and the next [tool.semantic_release]
        content = content.split("[tool.ruff]")[1].split("[tool.semantic_release]")[0]
        content = "[tool.ruff]" + content

    with Path("pyproject.toml").open("w") as f:
        f.write(content)

    c.run("ruff check . --fix --config pyproject.toml")


@task
def pr(c: Context):
    """Create a pull request on GitHub."""
    lint(c)
    test_instantiation(c)
