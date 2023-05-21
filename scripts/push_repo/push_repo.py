#!/usr/bin/env python

import argparse
import os
from github import Github
from github_secrets import GITHUB_API_TOKEN

parser = argparse.ArgumentParser(description='pushes an existing local repository to a remote repository on GitHub')
parser.add_argument('path', metavar='PATH', type=str, help='Enter the path to the local repository')
parser.add_argument('repo', metavar='REPO', type=str, help='Enter the name of the remote repository')
args = parser.parse_args()

path = args.path
repo = args.repo

# Retrieve GitHub access token from environment variable or enter it directly
if not GITHUB_API_TOKEN:
    GITHUB_API_TOKEN = input('Enter your GitHub access token: ')

# Create a GitHub instance using the access token
g = Github(GITHUB_API_TOKEN)

# Get the authenticated user
user = g.get_user()

# Retrieve the local repository name
local_repo = os.path.basename(path)

# Change to the local repository directory
os.chdir(path)

# Initialize Git repository and perform initial commit
os.system('git init')
os.system('git add .')
os.system('git commit -m "Initial commit"')

# Create the remote repository
remote_repo = user.create_repo(repo)

# Add the remote repository and push the local repository to it
os.system(f'git remote add origin {remote_repo.clone_url}')
os.system('git push -u origin master')

print("Pushing complete!")
print(f"\nREMOTE URL FOR \"{repo}\" is: {remote_repo.html_url}")
