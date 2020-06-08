#!/usr/bin/env bash
set -e

INSTALL_DIR='/opt/git_inspector'
CURRENT_PATH=$(realpath $(dirname ${BASH_SOURCE[0]}))

if [[ ! -d ${INSTALL_DIR} ]]
then
    echo "git_inspector is not installed"
    exit 1
fi

# copy and install venv
sudo rm -rf ${INSTALL_DIR}

# link path
sudo rm /usr/local/bin/git_inspector

echo -e "\e[92mun_installed git_inspector\e[39m"

