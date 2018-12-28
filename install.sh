#!/usr/bin/env bash
# if some command exit non zero, stop installation
set -e

# install virtual environment
if [ ! -f venv ]
then
    python3 -pip install virtualenv
    virtualenv --python=python3 venv
fi


source venv/bin/activate

python3 -m pip install -r requirements.txt

deactivate