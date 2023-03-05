python -m venv .venv
source .venv/bin/activate

# If no commits exist, initialise the repo
if ! git rev-parse HEAD > /dev/null 2>&1; then
  git init
  git add .
  git commit -m "init: first commit"
fi

pre-commit install --install-hooks -t pre-push
pip install -e .[dev,tests]
