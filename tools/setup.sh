#!/bin/bash

# Copy the commit-msg hook to the .git/hooks directory
cp ./tools/commit-msg ./.git/hooks/

# create a virtual environment
virtualenv ./kb_venv

# activate the virtual environment
source ./kb_venv/bin/activate

# pip install the requirements
pip install --upgrade pip && pip install -r ./requirements/requirements.txt 

# install npm packages present in jstools/package.json
npm install --prefix ./jstools/