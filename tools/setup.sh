#!/bin/bash

# Copy the commit-msg hook to the .git/hooks directory
cp ./tools/commit-msg ./.git/hooks/

# pip install the requirements
pip install --upgrade pip && pip install -r ./requirements/requirements.txt 

# install npm packages present in jstools/package.json
npm install --prefix ./jstools/