# Create Issue by Python

import argparse
import requests
import json

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
if response.ok:
    # Issue created successfully
    issue_data = response.json()
    issue_number = issue_data.get('number')
    issue_url = issue_data.get('html_url')
    print("Issue created successfully!")
    print(f"Issue number: {issue_number}")
    print(f"Issue URL: {issue_url}")
else:
    # Issue creation failed
    error_message = response.json().get('message', 'Unknown error')
    error_status = response.status_code
    error_response = json.dumps(response.json(), indent=4)
    print(f"Failed to create issue. Error status: {error_status}")
    print(f"Error message: {error_message}")
    print("Error response:")
    print(error_response)

print("Thank you!")
# Issue Created
