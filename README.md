# swift-python-cookiecutter
A python package template intended for low maintenance and quick package development.

## Getting started

Install cruft
```
pip install cruft
```

Use template:
```
cd desired_project_folder
cruft create https://github.com/MartinBernstorff/swift-python-cookiecutter
```
This will create a folder `desired_project_folder/{package_name}` containing all the template files.

## Using git and GitHub

To initialize as a git repo simply use the git init command.
```bash
git init -b main    
```
If you want to add a remote like GitHub you can do so using the following command:
```
git remote add origin {repository url}
```

Where `repository url` is a link to an empty repository.

## Authors
- Kenneth Enevoldsen
- Martin Bernstorff
