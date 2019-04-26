#!/usr/bin/env bash
set -e

INSTALL_DIR='/opt/git_inspector'

if [[ ! -d ${INSTALL_DIR} ]]
then
    echo "git_inspector is not installed"
    exit 1
fi


# copy and install venv
rm -rf ${INSTALL_DIR}

# link path
sudo rm /usr/local/bin/git_inspector
