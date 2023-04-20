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


from invoke import Context, task

new_instance_dir = "swift-python"


@task
def setup(c: Context):
    """Setup while instantiating the project."""
    for invoke_command in ["setup", "install", "lint", "test", "docs"]:
        c.run(f"cd {new_instance_dir} && inv {invoke_command}")


@task
def cruft_create(c):
    c.run(f"rm -rf {new_instance_dir}")

    c.run("pip install cruft")
    c.run("cruft create . -y")


@task
def test_instantiation(c: Context):
    """Test that the project can be instantiated."""
    cruft_create(c)
    setup(c)


@task
def lint(c):
    c.run("black . --line-length 1000")
    c.run("ruff check . --isolated --fix --line-length=1000")
    # --isolated to ignore pyproject.toml with cookiecutter placeholders, which are not valid TOML


@task
def pr(c: Context):
    """Create a pull request on GitHub."""
    lint(c)
    test_instantiation(c)
