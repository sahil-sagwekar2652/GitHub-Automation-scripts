#!/bin/bash

printf "Cloning The Repository...\n"
git clone https://github.com/sahil-sagwekar2652/GitHub-Automation-scripts.git
cd ../scripts
touch github_secrets.py
echo 'Please enter your Github Username'
read github_account
echo -e '\n Please enter your Github Password'
read github_password
echo -e "GITHUB_API_TOKEN = '$github_account'\nUSERNAME = '$github_password'" > github_secrets.py
cd ..
echo 'export PATH=$PATH''":'"$(pwd)"'/scripts''"' >> ~/.bash_profile