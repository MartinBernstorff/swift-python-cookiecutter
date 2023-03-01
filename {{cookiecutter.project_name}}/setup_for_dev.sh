virtualenv .venv
source .venv/bin/activate
pip install -e .[dev,tests]
pre-commit install