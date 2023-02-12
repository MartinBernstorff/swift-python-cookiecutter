
# User Guide

This is the user guide
for the [Swift Python Cookiecutter] template.

If you're in a hurry, check out the [quickstart guide](quickstart)
and the [tutorials](tutorials).

## Introduction

### About this project

The Swift Python Cookiecutter is a general-purpose template for Python libraries.

The main objective of this project template is to enable current best practices
through modern Python tooling.

Our goals are to:

- promote code quality through automation, 
- provide reliable and repeatable processes,
- focus on the development experience,
- and be easy to modify and edit.

all the way from local testing to publishing releases.

Projects are created from the template using [Cookiecutter],
a project scaffolding tool built on top of the [Jinja] template engine.

The project template is centered around [GitHub Actions] for continuous
integration and delivery.

The swift-python-cookiecutter template is based on the [Hypermodern Python] template,
but with a few changes:

- The template has replaced scaffoliding code such as [nox]
- The template uses [semantic release] for versioning and publishing
- The template replaces [poetry] with pip as it is notably faster for larger projects.
- The template replaced a series of linting packages such as [flake8] with [ruff].

### Features

Here is a detailed list of features for this Python template:

```{eval-rst}
.. include:: ../README.md
   :start-after: <!-- features-begin -->
   :end-before: <!-- features-end -->

```


## Installation

### Requirements

To use this project you will need to have [git] and [Python] installed on your system.
Furthermore you will need to install [Cookiecutter] to create projects from the 
template:

```console
$ pip --user install cookiecutter
```

## Project creation

### Creating a project

Create a project from this template
by pointing Cookiecutter to its [GitHub repository][swift python cookiecutter]:

```console
$ cookiecutter gh:kennethenevoldsen/swift-python-cookiecutter
```

Cookiecutter downloads the template,
and asks you a series of questions about project variables,
for example, how you wish your project to be named.
When you have answered these questions,
your project is generated in the current directory,
using a subdirectory with the same name as your project.

Here is a complete list of the project variables defined by this template:

:::{list-table} Project variables
:header-rows: 1
:widths: auto

- - Variable
  - Description
  - Example
- - `project_name`
  - Project name on PyPI and GitHub
  - `swift-python`
- - `package_name`
  - Import name of the package
  - `swift_python`
- - `friendly_name`
  - Friendly project name
  - `Swift Python`
- - `author`
  - Primary author
  - Katherine Johnson
- - `email`
  - E-mail address of the author
  - katherine@example.com
- - `github_user`
  - GitHub username of the author
  - `katherine`
- - `version`
  - Initial project version
  - `0.0.0`
- - `copyright_year`
  - The project copyright year
  - `2022`
- - `license`
  - The project license
  - `MIT`
- - `development_status`
  - Development status of the project
  - `Development Status :: 3 - Alpha`

:::

:::{note}
The initial project version should be the latest release on [PyPI],
or `0.0.0` for an unreleased package.
See [The Release workflow](the-release-workflow) for details.
:::

Your choices are recorded in the file `.cookiecutter.json` in the generated project,
together with the URL of this Cookiecutter template.
Having this [JSON] file in the project makes it possible later on
to update your project with changes from the Cookiecutter template,
using tools such as [cupper].

In the remainder of this guide,
`<project>` and `<package>` are used
to refer to the project and package names, respectively.
By default, their only difference is that
the project name uses hyphens (_kebab case_),
whereas the package name uses underscores (_snake case_).

### Uploading to GitHub

This project template is designed for use with [GitHub].
After generating the project,
your next steps are to create a Git repository and upload it to GitHub.

Change to the root directory of your new project,
initialize a Git repository, and
create a commit for the initial project structure.
In the commands below,
replace `<project>` by the name of your project.

```console
$ cd <project>
$ git init
$ git add .
$ git commit
```

Use the following command to ensure your default branch is called `main`,
which is the [default branch name for GitHub repositories][github renaming].

```console
$ git branch --move --force main
```

Create an empty repository on [GitHub],
using the project name you chose when you generated the project.

:::{note}
Do not include a `README.md`, `LICENSE`, or `.gitignore`.
These files are provided by the project template.
:::

Finally, upload your repository to GitHub.
In the commands below, replace `<username>` by your GitHub username,
and `<project>` by the name of your project.

```console
$ git remote add origin git@github.com:<username>/<project>.git
$ git push --set-upstream origin main
```

Now may be a good time to set up Continuous Integration for your repository.
Refer to the section [External services](external-services)
for detailed instructions.

## Project overview

### Files and directories

This section provides an overview of all the files generated for your project.

Let's start with the directory layout:

:::{list-table} Directories
:widths: auto

- - `src/<package>`
  - Python package
- - `tests`
  - Test suite
- - `docs`
  - Documentation
- - `.github/workflows`
  - GitHub Actions workflows

:::

The Python package is located in the `src/<package>` directory.
For more details on these files, refer to the section [The initial package](the-initial-package).

:::{list-table} Python package
:widths: auto

- - `src/<project>/py.typed`
  - Marker file for [PEP 561][pep 561]
- - `src/<project>/__init__.py`
  - Package initialization

:::

The test suite is located in the `tests` directory.
For more details on these files, refer to the section [The test suite](the-test-suite).

:::{list-table} Test suite
:widths: auto

- - `tests/__init__.py`
  - Test package initialization

:::

The project documentation is written in [Markdown].
The documentation files in the top-level directory are rendered on [GitHub]:

:::{list-table} Documentation files (top-level)
:widths: auto

- - `README.md`
  - Project description for GitHub and PyPI

:::

The files in the `docs` directory are
built using [Sphinx](documentation) and [MyST-NB].
The Sphinx documentation is hosted using [GitHub pages].

:::{list-table} Documentation files (Sphinx)
:widths: auto

- - `index.md`
  - Main document
- - `faq.md`
  - Frequently asked questions, including frequently asked questions about the
    how to use the project
- - `usage.ipynb`
  - Usage guide in Jupyter Notebook format.
- - `reference.md`
  - API reference

:::

The `.github/workflows` directory contains the [GitHub Actions workflows](github-actions-workflows):

:::{list-table} GitHub Actions workflows
:widths: auto

- - `release.yml`
  - [The Release workflow](the-release-workflow)
- - `tests.yml`
  - [The Tests workflow](the-tests-workflow)
- - `documentation.yml`
  - [The Documentation workflow](the-documentation-workflow)
- - `dependabot_automerge.yml`
  - [The Dependabot automerge workflow](dependabot-integration)

:::

The project contains many configuration files for developer tools.
Most of these are located in the top-level directory.
The table below lists these files,
and links each file to a section with more details.

:::{list-table} Configuration files
:widths: auto

- - `.cookiecutter.json`
  - [Project variables](creating-a-project)
- - `.github/dependabot.yml`
  - Configuration for [Dependabot](dependabot-integration)
- - `.gitignore`
  - [Git ignore file][.gitignore]
- - `.pre-commit-config.yaml`
  - Configuration for [pre-commit](linting-with-pre-commit)
- - `docs/conf.py`
  - Configuration for [Sphinx](documentation)
- - `pyproject.toml`
  - Build configuration for your porject as well as [ruff], [mypy], etc.
:::

The `pyproject.toml` file is described in more detail [below](the-pyproject-toml-file).

:::


### The initial package

You can find the initial Python package in your generated project
under the `src` directory:

```
src
└── <package>
    ├── __init__.py
    └── py.typed
```

`__init__.py`

: This file declares the directory as a [Python package],
  and contains any package initialization code.

`py.typed`

: This is an empty marker file,
  which declares that your package supports typing
  and is distributed with its own type information
  ([PEP 561][pep 561]).
  This allows people using your package
  to type-check their Python code against it.


### The test suite

Tests are written using the [pytest] testing framework,
the _de facto_ standard for testing in Python.

The test suite is located in the `tests` directory:

```
tests
└── __init__.py
```

The test suite is [declared as a package][pytest layout],
and mirrors the source layout of the package under test.

For details on how to run the test suite,
refer to the section [The tests session](the-tests-session).

### Documentation

The project documentation is written in [Markdown]
and processed by the [Sphinx] documentation engine using the [MyST-NB] extension.

The top-level directory contains several stand-alone documentation files:

<!-- prettier-ignore-start -->

`README.md`

: This file is your main project page and displayed on GitHub and PyPI.

`CONTRIBUTING.md`

: The Contributor Guide explains how other people can contribute to your project.

`CODE_OF_CONDUCT.md`

: The Code of Conduct outlines the behavior
  expected from participants of your project.
  It is adapted from the [Contributor Covenant], version 2.1.

`LICENSE.md`

: This file contains the text of your project's license.

:::{note}
The files above are also rendered on GitHub and PyPI.
Keep them in plain Markdown, without [MyST-NB] syntax extensions.
:::

The documentation files in the `docs` directory are built using [Sphinx] and [MyST-NB]:

`index.md`

: This is the main documentation page.
  It includes the project description from `README.md`.
  This file also defines the navigation menu,
  with links to other documentation pages.

`reference.md`

: The API reference for your project.
  It is generated from docstrings and type annotations in the source code,
  using the [autodoc] and [napoleon] extensions.

`usage.ipynb`

: The usage guide for your project.
  It is written in [Jupyter Notebook] format,
  and converted to Markdown using [MyST-NB].

The `docs` directory contains two more files:

`conf.py`

: This Python file contains the [Sphinx configuration].

`requirements.txt`

: Additional requirements for building the docuementation which is not used by the
  package itself. Generally we recommend specifying the dependencies the 
  `pyproject.toml` file, under `optional-dependencies` under the `docs` key.
  However, if you need to specify dependencies which are not allowed in the
  `pyproject.toml` file (such as direct links), you can specify them in this file.

The project documentation is built and hosted on [Github Pages] and uses the
[furo] Sphinx theme.

You can also build the documentation locally using [Sphinx]. 
see [The docs session](the-docs-session).

## Packaging

### The pyproject.toml file

The configuration file for the Python package is located
in the root directory of the project,
and named `pyproject.toml`.
It uses the [TOML] configuration file format,
and contains two sections---_tables_ in TOML parlance---,
specified in [PEP 517][pep 517] and [518][pep 518]:

- The `build-system` table
  declares the requirements and the entry point
  used to build a distribution package for the project.
  This template uses [setuptools] as the build system.
- The `project` table
  contains the metadata for your package,
  such as its name, version, and authors,
  as well as the list of dependencies for the package. Please refer to the
  to the [setuptools documentation][setuptools configuration] for a detailed
  description of each configuration key.
- The `tool` table contains sub-tables
  where tools can store configuration under their [PyPI] name.

:::{list-table} Tool configurations in pyproject.toml
:widths: auto

- - `tool.coverage.run`
  - Configuration for [pytest-cov]
- - `tool.ruff`
  - Configuration for [ruff]
- - `tool.mypy`
  - Configuration for [mypy]
- - `tool.setuptools`
  - Configuration for [setuptools]
- - `tool.semantic_release`
  - Configuration for [semantic-release]

:::

### Version constraints

[Version constraints][versions and constraints] express
which versions of dependencies are compatible with your project.
In the case of core dependencies,
they are also a part of distribution packages,
and as such affect end-users of your package.

:::{note}
Dependencies are Python packages used by your project,
and they come in two types:

- _Core dependencies_ are required by users running your code,
  and typically consist of third-party libraries imported by your package.
  When your package is distributed,
  the [package metadata] includes these dependencies (under `project.dependencies`),
  allowing tools like [pip] to automatically install them alongside your package.
- _Development dependencies_ are only required by developers working on your code.
  Examples are applications used to run tests,
  check code for style and correctness,
  or to build documentation.
  These dependencies are not a part of distribution packages,
  because users do not require them to run your code. This templates includes these
  dependencies in the `project.optional-dependencies` under the keys `docs`, `tests`,
  `style`, and `tutorials`.

:::

For every dependency needed by your project you will need to specify 
a version constraint in the pyproject.toml file. Where you can specify a lower and
an upper bound for the version constraint.

- The lower bound requires users of your package to have at least the version
  that was current when you added the dependency.
- The upper bound allows users to upgrade to newer releases of dependencies,
  as long as the version number does not indicate a breaking change.

Whether you wish to specify a version constraint as exact version (`package==1.2.3"`),
a range (`package>=1.2.3,<1.3.0`), or as lower bound (`package>=1.2.3`), 
depends on the type of workflow you are using. If you wish to read more on this topic
please refer to the following articles:


- [Version numbers: how to use them?][gabor version] by Bernát Gábor
- [Semantic Versioning Will Not Save You][schlawack semantic] by Hynek Schlawack


:::{note}
The problem with upper bounds displayed in the articles is often minor as [dependabot]
automatically updates version constraints in `pyproject.toml`.
:::

### Dependencies

This project template has no a core dependencies, bu comes with various development
dependencies.
See the table below for an overview of the dependencies of generated projects:

:::{list-table} Dependencies
:widths: auto

- style
  - - [black]
    - The uncompromising code formatter.
  - - [ruff]
    - A super fast linting tool for Python projects. Including multiple linters. including
      [flake8], [isort], [pylint], [pydocstyle], etc..
  - - [mypy]
    - Optional static typing for Python
  - - [pre-commit]
    - A framework for managing and maintaining multi-language pre-commit hooks.
- tests
  - - [pytest-cov]
    - Code coverage measurement for Python
  - - [pytest]
    - pytest: simple powerful testing with Python
  - - [typeguard]
    - Run-time type checker for Python
- Docs:
  - - [furo]
    - A clean customisable Sphinx documentation theme.
  - - [sphinx]
    - Python documentation generator
  - - [myst-nb]
    -  A Sphinx extension for executing Jupyter notebooks in Sphinx.
 -  - [sphinx-copybutton]
    - A sphinx extension that adds a "copy" button to code blocks.
  - - [sphinxext-opengraph]
    - A Sphinx extension to generate Open Graph metadata.

:::

### The docs session

Build the documentation using using [sphinx]:

```bash
sphinx-build docs docs/_build
```


The command `sphinx-build` to generate the HTML documentation from the Sphinx directory.


### The tests session

Tests are written using the [pytest] testing framework.
Learn more about it in the section [The test suite](the-test-suite).

Run the test suite using session `pytest`:

```bash
pytest
```

Before you can run the tests you will need to have your project installed. You can do
this using:

```bash
pip install -e ".[tests]"
```

To get the coverage while running the tests you can use the `pytest-cov` plugin:

```bash
pytest --cov=src
```

You can also run the test using the [typeguard] plugin:

```bash
pytest --typeguard-packages=src
```

## Linting with pre-commit

[pre-commit] is a multi-language linter framework and a Git hook manager.
It allows you to
integrate linters and formatters into your Git workflow,
even when written in a language other than Python.

pre-commit is configured using the file `.pre-commit-config.yaml`
in the project directory.
Please refer to the [official documentation][pre-commit configuration]
for details about the configuration file.

### Running pre-commit

to initialize the pre-commit environment simply run:

```bash
pre-commit install
```

This will install the pre-commit hook into your local Git repository and they
will be run automatically every time you invoke `git commit`.

You can also run pre-commit manually:

```bash
pre-commit run
```

Which will run all the checks all the files in the commit. If you wish to run
the checks on all the files in the repository you can use the `--all-files` flag:

```bash
pre-commit run --all-files
```

### Adding an official pre-commit hook

Adding the official pre-commit hook for a linter is straightforward.
Often you can simply copy a configuration snippet from the repository's `README`.
Otherwise, note the hook identifier from the `pre-commit-hooks.yaml` file,
and the git tag for the latest version.
Add the following section to your `pre-commit-config.yaml`, under `repos`:

```yaml
- repo: <hook repository>
  rev: <version tag>
  hooks:
    - id: <hook identifier>
```

While this technique also works for Python-language hooks.


### Overview of pre-commit hooks

The swift python template comes with a pre-commit configuration consisting of the
following hooks:

:::{list-table} pre-commit hooks
:widths: auto

- - [black]
  - Run the [Black] code formatter
- - [rff]
  - Run the [ruff] linter
- - [check-toml]
  - Validate [TOML] files
- - [check-yaml]
  - Validate [YAML] files
- - [end-of-file-fixer]
  - Ensure files are terminated by a single newline
- - [trailing-whitespace]
  - Ensure lines do not contain trailing whitespace

:::

## Type-checking with mypy

:::{note}
[Type annotations], first introduced in Python 3.5,
are a way to annotate functions and variables with types.
With appropriate tooling,
they can make your programs easier to understand, debug, and maintain.

_Type-checking_ refers to the practice of
verifying the type correctness of a program,
using type annotations and type inference.
There are two kinds of type checkers:

- _Static type checkers_ verify the type correctness of your program
  without executing it, using static analysis.
- _Runtime type checkers_ find type errors by instrumenting your code to
  type-check arguments and return values in function calls.
  This is particularly useful during the execution of unit tests.

There is also an increasing number of libraries
that leverage type annotations at runtime.
For example, you can use type annotations to generate serialization schemas
or command-line parsers.
:::

[mypy] is the pioneer and _de facto_ reference implementation of static type checking in
Python. Most often mypy is integrated into the developers IDE, but it can also be
used as a command line tool simpyl by running:

```bash
mypy src
```

Where `src` is the directory containing the Python source code.


### PyPI

[PyPI] is the official Python Package Index.
Uploading your package to PyPI allows others to
download and install it to their system.

Follow these steps to set up PyPI for your repository:

1. Sign up at [PyPI].
2. Go to the Account Settings on PyPI,
   generate an API token, and copy it.
3. Go to the repository settings on GitHub, and
   add a secret named `PYPI_TOKEN` with the token you just copied.

PyPI is integrated with your repository
via the [Release workflow](the-release-workflow).


### Pre-commit.ci

**TODO: Add documentation here**


### Dependabot

[Dependabot] creates pull requests with automated dependency updates, by default it will
update all python dependencies in the repository.

Please refer to the [official documentation][dependabot docs] for more details.

The configuration is included in the repository, in the file [.github/dependabot.yml].



:::{list-table}
:header-rows: 1
:widths: auto

- - Type of dependency
  - Managed files
  - See also
- - Python
  - `poetry.lock`
  - [Managing dependencies](managing-dependencies)
- - Python
  - `docs/requirements.txt`
  - [Read the Docs](read-the-docs-integration)
- - Python
  - `.github/workflows/constraints.txt`
  - [Constraints file](workflow-constraints)
- - GitHub Action
  - `.github/workflows/*.yml`
  - [GitHub Actions workflows](github-actions-workflows)

:::

## GitHub Actions workflows

The swift python template uses[GitHub Actions]
to implement continuous integration and delivery.
With GitHub Actions,
you define so-called workflows
using [YAML] files located in the `.github/workflows` directory.

A _workflow_ is an automated process
consisting of one or many jobs,
each of which executes a series of steps.
Workflows are triggered by events,
for example when a commit is pushed
or when a release is published.
You can learn more about
the workflow language and its supported keywords
in the [official reference][github actions syntax].

:::{note}
Real-time logs for workflow runs are available
from the _Actions_ tab in your GitHub repository.
:::

### Overview of workflows

The swift python template defines the following workflows:

:::{list-table} GitHub Actions workflows
:header-rows: 1
:widths: auto

- - Workflow
  - File
  - Description
  - Trigger
- - [Tests](the-tests-workflow)
  - `tests.yml`
  - Run the test suite, notebooks on Linux, macOS, and Windows and create a coverage comment on the PR
  - Push, PR
- - [Release](the-release-workflow)
  - `release.yml`
  - Update the version number, create a release on GitHub, and upload the package to [PyPI] 
  - Push
- - [Documentation](the-documentation-workflow)
  - `documentation.yml`
  - Build the documentation and if it is the main branch pushes it to the `gh-pages` branch
  - Push, PR
- - [Automerge](the-automerge-workflow)
  - `automerge.yml`
  - Automatically merge PRs that have the `automerge` label
  - PR created by Dependabot

:::


### The Tests workflow

**TODO: Add documentation here**

### The Release workflow

**TODO: Add documentation here**


### The Documentation workflow

**TODO: Add documentation here**

### The Automerge workflow

**TODO: Add documentation here**

(tutorials)=

## Tutorials

First, make sure you have all the [requirements](installation) installed.

### How to test your project

To run the tests in the project simply run using [typeguard] and [pytest-cov]:

```bash
pytest --cov=src --cov-report=term-missing --typeguard-packages=src
```

### How to push code changes

:::{note}
Nowadays it is luckily quite common to use a IDE to manage git commits and
thus these steps can't often be skipped. It is however nice to know that
these steps are the same as the ones you would use in the terminal.
:::

Create a branch for your changes:

```bash
git branch my-new-branch
git checkout my-new-branch
```

Create a series of small, single-purpose commits:

```console
$ git add <files>
$ git commit -m "A description of your changes"
```

Push your branch to GitHub:

```console
$ git push
```

The push triggers the pre-commit hooks and pushes the changed to the remote GitHub
repository.


### How to open a pull request

Open a pull request for your branch on GitHub:

1. Select your branch from the _Branch_ menu.
2. Click **New pull request**.
3. Enter the title for the pull request.
4. Enter a description for the pull request.
5. Click **Create pull request**.
6. Potentially add reviewers to the pull request.


[--reuse-existing-virtualenvs]: https://nox.thea.codes/en/stable/usage.html#re-using-virtualenvs
[.gitattributes]: https://git-scm.com/book/en/Customizing-Git-Git-Attributes
[.github/dependabot.yml]: https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates
[.gitignore]: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring
[.readthedocs.yml]: https://docs.readthedocs.io/en/stable/config-file/v2.html
[2022.6.3]: https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases/tag/2022.6.3
[__main__]: https://docs.python.org/3/library/__main__.html
[abstract syntax tree]: https://docs.python.org/3/library/ast.html
[actions/cache]: https://github.com/actions/cache
[actions/checkout]: https://github.com/actions/checkout
[actions/download-artifact]: https://github.com/actions/download-artifact
[actions/setup-python]: https://github.com/actions/setup-python
[actions/upload-artifact]: https://github.com/actions/upload-artifact
[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit codes]: https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing
[bandit]: https://github.com/PyCQA/bandit
[bash]: https://www.gnu.org/software/bash/
[batchelder include]: https://nedbatchelder.com/blog/202008/you_should_include_your_tests_in_coverage.html
[black]: https://github.com/psf/black
[calendar versioning]: https://calver.org
[cannon semver]: https://snarky.ca/why-i-dont-like-semver/
[check-added-large-files]: https://github.com/pre-commit/pre-commit-hooks#check-added-large-files
[check-toml]: https://github.com/pre-commit/pre-commit-hooks#check-toml
[check-yaml]: https://github.com/pre-commit/pre-commit-hooks#check-yaml
[click.testing.clirunner]: https://click.palletsprojects.com/en/7.x/testing/
[click]: https://click.palletsprojects.com/
[cobertura]: https://cobertura.github.io/cobertura/
[codecov configuration]: https://docs.codecov.io/docs/codecov-yaml
[codecov/codecov-action]: https://github.com/codecov/codecov-action
[codecov]: https://codecov.io/
[constraints file]: https://pip.pypa.io/en/stable/user_guide/#constraints-files
[contributor covenant]: https://www.contributor-covenant.org
[cookiecutter]: https://github.com/audreyr/cookiecutter
[coverage.py]: https://coverage.readthedocs.io/
[crazy-max/ghaction-github-labeler]: https://github.com/crazy-max/ghaction-github-labeler
[cupper]: https://github.com/senseyeio/cupper
[curl]: https://curl.haxx.se
[cyclomatic complexity]: https://en.wikipedia.org/wiki/Cyclomatic_complexity
[darglint codes]: https://github.com/terrencepreilly/darglint#error-codes
[darglint]: https://github.com/terrencepreilly/darglint
[dependabot docs]: https://docs.github.com/en/github/administering-a-repository/keeping-your-dependencies-updated-automatically
[dependabot issue 4435]: https://github.com/dependabot/dependabot-core/issues/4435
[dependabot]: https://dependabot.com/
[dev-prod parity]: https://12factor.net/dev-prod-parity
[editable install]: https://pip.pypa.io/en/stable/cli/pip_install/#install-editable
[end-of-file-fixer]: https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer
[flake8 configuration]: https://flake8.pycqa.org/en/latest/user/configuration.html
[flake8-bandit]: https://github.com/tylerwince/flake8-bandit
[flake8-bugbear codes]: https://github.com/PyCQA/flake8-bugbear#list-of-warnings
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8-docstrings]: https://gitlab.com/pycqa/flake8-docstrings
[flake8-rst-docstrings codes]: https://github.com/peterjc/flake8-rst-docstrings#flake8-validation-codes
[flake8-rst-docstrings]: https://github.com/peterjc/flake8-rst-docstrings
[flake8]: http://flake8.pycqa.org
[furo]: https://pradyunsg.me/furo/
[future imports]: https://docs.python.org/3/library/__future__.html
[gabor version]: https://bernat.tech/posts/version-numbers/
[git hook]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
[git]: https://www.git-scm.com
[github actions artifacts]: https://help.github.com/en/actions/configuring-and-managing-workflows/persisting-workflow-data-using-artifacts
[github actions runners]: https://help.github.com/en/actions/automating-your-workflow-with-github-actions/virtual-environments-for-github-hosted-runners#supported-runners-and-hardware-resources
[github actions syntax]: https://help.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[github release]: https://help.github.com/en/github/administering-a-repository/about-releases
[github renaming]: https://github.com/github/renaming
[github]: https://github.com/
[google docstring style]: https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
[hypermodern python blog]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
[hypermodern python chapter 1]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[hypermodern python chapter 2]: https://medium.com/@cjolowicz/hypermodern-python-2-testing-ae907a920260
[hypermodern python chapter 3]: https://medium.com/@cjolowicz/hypermodern-python-3-linting-e2f15708da80
[hypermodern python chapter 4]: https://medium.com/@cjolowicz/hypermodern-python-4-typing-31bcf12314ff
[hypermodern python chapter 5]: https://medium.com/@cjolowicz/hypermodern-python-5-documentation-13219991028c
[hypermodern python chapter 6]: https://medium.com/@cjolowicz/hypermodern-python-6-ci-cd-b233accfa2f6
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[hypermodern python]: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
[import hook]: https://docs.python.org/3/reference/import.html#import-hooks
[install-poetry.py]: https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py
[isort black profile]: https://pycqa.github.io/isort/docs/configuration/black_compatibility.html
[isort force_single_line]: https://pycqa.github.io/isort/docs/configuration/options.html#force-single-line
[isort lines_after_imports]: https://pycqa.github.io/isort/docs/configuration/options.html#lines-after-imports
[isort]: https://pycqa.github.io/isort/
[jinja]: https://palletsprojects.com/p/jinja/
[json]: https://www.json.org/
[markdown]: https://spec.commonmark.org/current/
[mccabe codes]: https://github.com/PyCQA/mccabe#plugin-for-flake8
[mccabe]: https://github.com/PyCQA/mccabe
[mit license]: https://opensource.org/licenses/MIT
[mypy configuration]: https://mypy.readthedocs.io/en/stable/config_file.html
[mypy]: http://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox-poetry]: https://nox-poetry.readthedocs.io/
[nox]: https://nox.thea.codes/
[package metadata]: https://packaging.python.org/en/latest/specifications/core-metadata/
[pep 257]: http://www.python.org/dev/peps/pep-0257/
[pep 440]: https://www.python.org/dev/peps/pep-0440/
[pep 517]: https://www.python.org/dev/peps/pep-0517/
[pep 518]: https://www.python.org/dev/peps/pep-0518/
[pep 561]: https://www.python.org/dev/peps/pep-0561/
[pep 8]: http://www.python.org/dev/peps/pep-0008/
[pep8-naming codes]: https://github.com/pycqa/pep8-naming#pep-8-naming-conventions
[pep8-naming]: https://github.com/pycqa/pep8-naming
[pip install]: https://pip.pypa.io/en/stable/reference/pip_install/
[pip]: https://pip.pypa.io/
[pipx]: https://pipxproject.github.io/pipx/
[poetry add]: https://python-poetry.org/docs/cli/#add
[poetry env]: https://python-poetry.org/docs/managing-environments/
[poetry export]: https://python-poetry.org/docs/cli/#export
[poetry install]: https://python-poetry.org/docs/cli/#install
[poetry remove]: https://python-poetry.org/docs/cli/#remove
[poetry run]: https://python-poetry.org/docs/cli/#run
[poetry show]: https://python-poetry.org/docs/cli/#show
[poetry update]: https://python-poetry.org/docs/cli/#update
[poetry version]: https://python-poetry.org/docs/cli/#version
[poetry]: https://python-poetry.org/
[pre-commit autoupdate]: https://pre-commit.com/#pre-commit-autoupdate
[pre-commit configuration]: https://pre-commit.com/#adding-pre-commit-plugins-to-your-project
[pre-commit repository-local hooks]: https://pre-commit.com/#repository-local-hooks
[pre-commit system hooks]: https://pre-commit.com/#system
[pre-commit-hooks]: https://github.com/pre-commit/pre-commit-hooks
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pycodestyle codes]: https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
[pycodestyle]: https://pycodestyle.pycqa.org/en/latest/
[pydocstyle codes]: http://www.pydocstyle.org/en/stable/error_codes.html
[pydocstyle]: http://www.pydocstyle.org/
[pyenv wiki]: https://github.com/pyenv/pyenv/wiki/Common-build-problems
[pyenv]: https://github.com/pyenv/pyenv
[pyflakes codes]: https://flake8.pycqa.org/en/latest/user/error-codes.html
[pyflakes]: https://github.com/PyCQA/pyflakes
[pygments]: https://pygments.org/
[pypa/gh-action-pypi-publish]: https://github.com/pypa/gh-action-pypi-publish
[pypi]: https://pypi.org/
[pyproject.toml]: https://python-poetry.org/docs/pyproject/
[pytest layout]: https://docs.pytest.org/en/latest/explanation/goodpractices.html#choosing-a-test-layout-import-rules
[pytest]: https://docs.pytest.org/en/latest/
[python build]: https://python-poetry.org/docs/cli/#build
[python package]: https://docs.python.org/3/tutorial/modules.html#packages
[python publish]: https://python-poetry.org/docs/cli/#publish
[python website]: https://www.python.org/
[pyupgrade]: https://github.com/asottile/pyupgrade
[read the docs]: https://readthedocs.org/
[readthedocs webhooks]: https://docs.readthedocs.io/en/stable/webhooks.html
[relative imports]: https://docs.python.org/3/reference/import.html#package-relative-imports
[release drafter]: https://github.com/release-drafter/release-drafter
[release-drafter/release-drafter]: https://github.com/release-drafter/release-drafter
[requirements file]: https://pip.readthedocs.io/en/stable/user_guide/#requirements-files
[restructuredtext]: https://docutils.sourceforge.io/rst.html
[safety]: https://github.com/pyupio/safety
[salsify/action-detect-and-tag-new-version]: https://github.com/salsify/action-detect-and-tag-new-version
[schlawack semantic]: https://hynek.me/articles/semver-will-not-save-you/
[schreiner constraints]: https://iscinumpy.dev/post/bound-version-constraints/
[schreiner poetry]: https://iscinumpy.dev/post/poetry-versions/
[semantic versioning]: https://semver.org/
[sphinx configuration]: https://www.sphinx-doc.org/en/master/usage/configuration.html
[sphinx-autobuild]: https://github.com/executablebooks/sphinx-autobuild
[sphinx-click]: https://sphinx-click.readthedocs.io/
[sphinx]: http://www.sphinx-doc.org/
[test fixture]: https://docs.pytest.org/en/latest/explanation/fixtures.html#about-fixtures
[testpypi]: https://test.pypi.org/
[toml]: https://github.com/toml-lang/toml
[tox]: https://tox.readthedocs.io/
[trailing-whitespace]: https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace
[type annotations]: https://docs.python.org/3/library/typing.html
[typeguard]: https://github.com/agronholm/typeguard
[unix-style line endings]: https://en.wikipedia.org/wiki/Newline
[versions and constraints]: https://python-poetry.org/docs/dependency-specification/
[virtual environment]: https://docs.python.org/3/tutorial/venv.html
[virtualenv]: https://virtualenv.pypa.io/
[wheel]: https://www.python.org/dev/peps/pep-0427/
[xdoctest]: https://github.com/Erotemic/xdoctest
[yaml]: https://yaml.org/
