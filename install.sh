#!/usr/bin/env bash
set -e

INSTALL_DIR='/opt/git_inspector'
EXECUTABLE_LINK='/usr/local/bin/git_inspector'
CURRENT_PATH=$(realpath $(dirname ${BASH_SOURCE[0]}))


if [ ${CURRENT_PATH} == ${INSTALL_DIR} ]
then
   echo -e "\e[33malready in ${INSTALL_DIR}, skip copying to ${INSTALL_DIR}"
   # expect repository is already copied to ${INSTALL_DIR}
   # skip copying to ${INSTALL_DIR}
else
    if [[ -d ${INSTALL_DIR} ]]
    then
	echo -e "\e[41mFolder ${INSTALL_DIR} already exists\e[0m"
	echo -n "update git_inspector? [y/n]"
	read -n 1 SHOULD_UPDATE
	echo ""
	if [ ${SHOULD_UPDATE} == "y" ]
	then
	    ./un_install.sh
	else
	    echo -e "\e[91mabort installation"
	    exit 1
	fi
    fi
    # copy current directory to INSTALL_DIR
    sudo mkdir ${INSTALL_DIR}
    sudo cp -r . ${INSTALL_DIR}
fi

# install python requirements
cd ${INSTALL_DIR}
python3 -m pip install -r requirements.txt > /dev/null


# link path
if [[ -f ${EXECUTABLE_LINK} ]]
then
    sudo rm ${EXECUTABLE_LINK}
fi
sudo ln -s ${INSTALL_DIR}/git_inspector.py /usr/local/bin/git_inspector

echo -e "\e[92minstalled git_inspector\e[39m"

if [ ${CURRENT_PATH} != ${INSTALL_DIR} ]
then
    echo "you can remove this directory"
fi

