<a href="https://github.com/kennethenevoldsen/swift-python-cookiecutter"><img src="https://github.com/kennethenevoldsen/swift-python-cookiecutter/blob/main/docs/_static/icon.png" width="100" align="right" /></a>

# swift-python-cookiecutter

<!-- badges-begin -->

[![Python Version][python version badge]][github page]
[![License][license badge]][license]
[![documentation][documentation badge]][documentation page]
[![Tests][github test badge]][github actions page]
[![Black codestyle][black badge]][black project]
[![tests](https://github.com/centre-for-humanities-computing/DaCy/actions/workflows/tests.yml/badge.svg)](https://github.com/centre-for-humanities-computing/Dacy/actions)

[github test badge]: https://github.com/kennethenevoldsen/swift-python-cookiecutter/actions/workflows/tests.yml/badge.svg
[documentation badge]: https://github.com/kennethenevoldsen/swift-python-cookiecutter/actions/workflows/documentation.yml/badge.svg
[documentation page]: https://kennethenevoldsen.github.io/swift-python-cookiecutter/
[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black project]: https://github.com/psf/black
[github actions page]: https://github.com/kennethenevoldsen/swift-python-cookiecutter/actions
[github page]: https://github.com/kennethenevoldsen/swift-python-cookiecutter
[license badge]: https://img.shields.io/github/license/kennethenevoldsen/swift-python-cookiecutter
[license]: https://github.com/kennethenevoldsen/swift-python-cookiecutter/blob/main/LICENSE
[python version badge]: https://img.shields.io/badge/Python-%3E=3.7-blue

<!-- badges-end -->


[Cookiecutter] template for a Python package inspired by 
[Hypermodern Python] cookiecutter template.

✨📚✨ [Read the full documentation][documentation page] ✨📚✨

[cookiecutter]: https://github.com/audreyr/cookiecutter
[hypermodern python]: https://github.com/cjolowicz/cookiecutter-hypermodern-python

## Usage
<!-- usage-begin -->

```console
$ cookiecutter gh:kennethenevoldsen/swift-python-cookiecutter
```
<!-- usage-ends -->

The template supports Python >3.7.

## Features
<!-- features-begin -->


### Packaging
- Packaging and dependency management using the much faster (and much more classy) pip
- Automated uploads to [PyPI]


### Documentation
- Documentation with [Sphinx], 
- Using [MyST-NB] for rendering notebooks and 
- using the [furo] theme 
- Generate API documentation with [napoleon]

### Style
- Format an linting with [pre-commit] using:
- [ruff] for linting and upgrading python syntax (previously handled by pyupgrade), sort imports (previously handled by isort).
- [black] for code formatting 

### Testing
- Static type-checking with [mypy]
- Testing with [pytest]
- Code coverage with [pytest-cov]
- Runtime type-checking with [Typeguard]

### Continuous Integration
- Continuous integration with [GitHub Actions]
- Automated dependency updates with [Dependabot] 
  - and automerge these if they pass the tests. Avoid the hassle manually merging these
- Automatic version bumbs, release notes and changelogs using [semantic release].

### Difference from Hypermodern Python

The following is the difference between this template and the [Hypermodern Python] template.

- ~~Packaging and dependency management with [Poetry]~~
  - We use the much faster (and much more classy) pip.
- ~~Test automation with [Nox]~~
  - We found that Nox added a lot uneeded complexity to the project and especially for new developers it created an additional barrier to entry. We therefore decided to use the standard python tooling for testing.
- Linting with ~~[Flake8]~~
  - We use [ruff] instead of Flake8. Ruff is notably faster and also implements rules from pycodestyle and similar tools.
- Documentation with [Sphinx], [MyST], and ~~[Read the Docs]~~ using the [furo] theme
  - While we still use a similar documentation setup, we use [GitHub pages] instead of Read the Docs as it allows for more flexibility.
- Code formatting with [Black] and ~~[Prettier]~~
- ~~Security audit with [Bandit] and [Safety]~~
  - We use GitHubs [dependabot] for security updates instead of Bandit and Safety.
- ~~Import sorting with [isort]~~
  - isort is implemented in ruff.
- ~~Code coverage with [Coverage.py]~~
  - We use [pytest-cov] instead of Coverage.py.
- ~~Coverage reporting with [Codecov]~~
    - We use [GitHub Actions] instead of Codecov and do not display the coverage badge in the README as we believe that it is not a good metric for the quality of the code and leads to problematic behavior.
- ~~Command-line interface with [Click]~~
  - We do not add a command-line interface by default. We believe that it is better to add it when it is needed.
- ~~Automated Python syntax upgrades with [pyupgrade]~~
  - Implemented in [ruff].
- ~~Check documentation examples with [xdoctest]~~
  - We do not run tests on the docstring. Docstrings are intended for documentation and if they are tested they will often require more complex code than is needed for the documentation, thus making the documentation harder to read.
- ~~Automated release notes with [Release Drafter]~~ 
  - We do not use release drafter but uses [semantic release] instead to automatically create releases and changelogs.


[pytest-cov]: https://pypi.org/project/pytest-cov/
[bandit]: https://github.com/PyCQA/bandit
[black]: https://github.com/psf/black
[click]: https://click.palletsprojects.com/
[codecov]: https://codecov.io/
[coverage.py]: https://coverage.readthedocs.io/
[dependabot]: https://dependabot.com/
[flake8]: http://flake8.pycqa.org
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[isort]: https://pycqa.github.io/isort/
[mypy]: http://mypy-lang.org/
[myst-nb]: https://myst-nb.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pypi]: https://pypi.org/
[pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[read the docs]: https://readthedocs.org/
[release drafter]: https://github.com/release-drafter/release-drafter
[safety]: https://github.com/pyupio/safety
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest
[ruff]: https://github.com/charliermarsh/ruff
[github pages]: https://pages.github.com/
<!-- features-end -->