#!/usr/bin/env bash

# cd in dir of this script
cd "$(dirname "$0")"

source venv/bin/activate

python3 git_inspector.py

deactivate
