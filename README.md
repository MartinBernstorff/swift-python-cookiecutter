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


## Recommened setup for the repository

To see the recommended setup for the repository, see the following file:
`{{cookiecutter.project_name}}/.github/recommended_repo_setup.md`

## Examples
Examples of projects using this template
<!-- this is nice to have for personal use just 
just help me find project that have dealt with the same issues as me

it does not need to be up to date
 -->
- [psycop-model-evaluation](https://github.com/Aarhus-Psychiatry-Research/psycop-model-evaluation)
- Martin's [Personal Mnemonic Medium](https://github.com/MartinBernstorff/personal-mnemonic-medium/)

## Authors
- Kenneth Enevoldsen
- Martin Bernstorff
