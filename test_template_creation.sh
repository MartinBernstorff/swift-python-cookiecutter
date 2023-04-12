#!/bin/sh
pip install cruft

# create project using template
cruft create . -y 

# run setup (install, lint, etc.)
cd swift-python
chmod +x .github/first_setup.sh
sh .github/first_setup.sh