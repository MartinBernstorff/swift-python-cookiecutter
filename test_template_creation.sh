#!/bin/sh
pip install cruft
cruft create . -y 
cd swift-python
chmod +x .github/first_setup.sh
sh .github/first_setup.sh