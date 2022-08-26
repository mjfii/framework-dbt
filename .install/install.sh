#!/bin/bash

# get git root and change to working directory
GIT_ROOT=$(git rev-parse --show-toplevel)
cd "${GIT_ROOT}" || exit
source ./.install/common/bash/loader.sh
echo "Installing dbt framework here: ${GIT_ROOT}"

# begin the install
initialize "trunc_log $GIT_ROOT" "Truncate Install Log"
initialize "build_venv $GIT_ROOT" "Build Virtual Environment"
initialize "install_pip $GIT_ROOT" "Install pip"
initialize "define_libs $GIT_ROOT" "Define Python Requirements"
initialize "install_libs $GIT_ROOT" "Install Python Requirements"
initialize "create_project $GIT_ROOT" "Create Project"
initialize "append_profile $GIT_ROOT" "Append Profile"
