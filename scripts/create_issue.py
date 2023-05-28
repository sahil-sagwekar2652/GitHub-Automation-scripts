# Create Issue by Python

import argparse
import requests

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Create a GitHub issue')
parser.add_argument('owner', type=str, help='Repository owner')
parser.add_argument('repo', type=str, help='Repository name')
parser.add_argument('title', type=str, help='Issue title')
parser.add_argument('description', type=str, help='Issue description')
parser.add_argument('token', type=str, help='GitHub API token')
args = parser.parse_args()

# Get the command-line arguments
owner = args.owner
repo = args.repo
title = args.title
description = args.description
token = args.token

# Set the GitHub API endpoint for creating an issue
url = f"https://api.github.com/repos/{owner}/{repo}/issues"

# Set the headers with the API token for authentication
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Set the issue data
data = {
    "title": title,
    "body": description
}

# Send a POST request to create the issue
response = requests.post(url, headers=headers, json=data)

# Check the response status code
if response.status_code == 201:
    # Issue created successfully
    print("Issue created successfully.")
else:
    # Issue creation failed
    print("Failed to create issue.")

print("Thank You")

# Issue Created
print()

