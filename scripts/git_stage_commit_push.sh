#!/bin/bash

# Prompt the user to enter the repository URL
read -p "Enter the repository URL: " repo_url

# Clone the repository with temp_repo name
git clone $repo_url temp_repo

# Change to the repository directory
cd temp_repo

# Prompt the user to enter the file path to be staged
read -p "Enter the files path to be staged (separated by space): " files

# Move all the files to the temp_repo folder 
mv -f $files .
# Add the files to the staging area
git add .

# Prompt the user to enter the commit message
read -p "Enter the commit message: " commit_message

# Commit the changes with the provided commit message
git commit -m "$commit_message"

# Prompt the user to enter the branch name
read -p "Enter the branch name: " branch

# Push the changes to the repository
git push -u origin $branch

# Clean up the temporary repository directory
cd ..
rm -rf temp_repo
