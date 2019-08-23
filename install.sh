#!/usr/bin/env bash
set -e


INSTALL_DIR='/opt/git_inspector'


if [[ -d ${INSTALL_DIR} ]]
then
    echo "git_inspector is already installed"
    exit 1
fi

# copy and install venv
sudo mkdir ${INSTALL_DIR}
sudo cp -r . ${INSTALL_DIR}
cd ${INSTALL_DIR}
python3 -m pip install -r requirements.txt


# link path
sudo ln -s ${INSTALL_DIR}/git_inspector.py /usr/local/bin/git_inspector
