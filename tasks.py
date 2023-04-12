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


@task
def test(c: Context):
    """Run tests of instantiating the project."""
    new_instance_dir = "swift-python"
    c.run(f"rm -rf {new_instance_dir}")
    c.run("pip install cruft")
    c.run("cruft create . -y")
    c.run(f"chmod +x {new_instance_dir}/.github/first_setup.sh")
    c.run(f"cd {new_instance_dir} && .github/first_setup.sh")
    c.run(f"rm -rf {new_instance_dir}")