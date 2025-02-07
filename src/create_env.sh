#!/bin/bash

# TO BE ABLE CONDA INSIDE THE SCRIPT
eval "$(conda shell.bash hook)"

# LOAD CONFIG AND ENV
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
CONFIG_FILE=$(realpath "$SCRIPT_DIR/../config/demo.config")
echo "Loading config from $CONFIG_FILE"
. $CONFIG_FILE # to load CONDA_ENV and PY_VERSION

# # STEPS
conda activate base
conda remove -n $CONDA_ENV --all -y
conda create --name $CONDA_ENV python=$PY_VERSION -y

# HELPER COMMANDS TO CONNECT TO THE ENV
conda env list
echo "conda activate $CONDA_ENV"