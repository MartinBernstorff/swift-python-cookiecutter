#!/bin/sh
# Bash file for automatically doing the full setup on first run
# Super handy when checking if the template works locally,
# Also used by create_new_project.yml in git workflows
set -e
pip install invoke
inv setup
source .venv/bin/activate
inv install
inv lint
inv test
inv docs