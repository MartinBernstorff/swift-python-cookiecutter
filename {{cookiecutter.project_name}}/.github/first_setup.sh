# Bash file for automatically doing the full setup on first run
# Super handy when checking if the template works locally,
# Also used by create_new_project.yml in git workflows
pip install invoke
inv setup
source .venv39/bin/activate
inv install
inv lint
inv docs