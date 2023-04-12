#!/bin/sh
# Bash file for automatically doing the full setup on first run
# Super handy when checking if the template works locally,
# Also used by .github/workflows/test_creating_template_instance.yml
set -e
ls -la
pip install invoke
inv setup
inv install
inv lint
inv test
inv docs