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


import shutil
from pathlib import Path

from invoke import Context, task

new_instance_dir = Path("swift-python")


@task
def setup_instance(c: Context):
    """Setup while instantiating the project."""
    with c.cd(new_instance_dir):
        for invoke_command in ["setup", "install", "lint", "test", "docs"]:
            c.run(f"inv {invoke_command}")


@task
def cruft_create(c: Context):
    if shutil.which("cruft") is None:
        c.run("pip install cruft")
    c.run("cruft create . -y")


@task
def test(c: Context):
    """Test that the project can be instantiated."""
    if new_instance_dir.exists():
        shutil.rmtree(new_instance_dir)

    cruft_create(c)
    setup_instance(c)


@task
def lint(c: Context):
    top_toml_path = Path("pyproject.toml")
    top_toml_path.unlink()
    c.run("black .")

    # Copy the file from {\{\{cookiecutter.project_name\}\}}/pyproject.toml to pyproject.toml
    shutil.copy(Path("{{cookiecutter.project_name}}/pyproject.toml"), top_toml_path)

    # Remove all lines starting with {% and ending with %}
    with top_toml_path.open("r") as f:
        content = f.read()
        content = "\n".join(
            [line for line in content.split("\n") if not line.startswith("{%")],
        )

        # Keep only stuffbetween [tool.ruff] and the next [tool.semantic_release]
        content = content.split("[tool.ruff]")[1].split("[tool.semantic_release]")[0]
        content = "[tool.ruff]" + content

    with top_toml_path.open("w") as f:
        f.write(content)

    c.run("ruff check . --fix --config pyproject.toml")


@task
def pr(c: Context):
    """Create a pull request on GitHub."""
    lint(c)
    test(c)
    c.run("gh pr create -w")
