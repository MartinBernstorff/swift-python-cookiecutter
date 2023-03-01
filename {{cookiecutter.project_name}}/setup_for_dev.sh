virtualenv .venv
source .venv/bin/activate
pip install -e .[dev]
pre-commit install