# swift-python-cookiecutter
A python package template intended for low maintenance and quick package development.

## Getting started

Install cruft
```
pip install cruft
```

Use template:
```bash
cruft create https://github.com/MartinBernstorff/swift-python-cookiecutter
```
This will create a folder named `{package_name}` containing all the template files.

## Using git and GitHub
To initialize as a git repo simply use the git init command.
```bash
cd {package_name}
git init -b main    
```

Or, if you want to get started with `Invoke`, an alternative to make:
```bash
pip install invoke
cd {package_name}
inv setup
```

If you want to add a remote like GitHub you can do so using the following command:
```
git remote add origin {repository url}
```

Where `repository url` is a link to an empty repository.


## Recommended setup for the repository
To see the recommended setup for the repository, see the following file:
`{package_name}/.github/recommended_repo_setup.md`

## Examples
Examples of projects using this template

- [The PSYCOP ML in healthcare project](https://github.com/Aarhus-Psychiatry-Research/psycop-common)
- Martin's [Personal Mnemonic Medium](https://github.com/MartinBernstorff/personal-mnemonic-medium/)

## Authors
- Kenneth Enevoldsen
- Martin Bernstorff
