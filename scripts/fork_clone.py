# Fork and Clone by Python

import argparse
import requests
import json
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Fork a repo')
parser.add_argument('owner', type=str, help='Repository owner')
parser.add_argument('repo', type=str, help='Repository name')
parser.add_argument('token', type=str, help='GitHub API token')
parser.add_argument('name',type=str,help='Enter name for forked repo')
args = parser.parse_args()

# Get the command-line arguments
owner = args.owner
repo = args.repo
token = args.token
name=args.name

# Set the GitHub API endpoint for forking a repo
url = f"https://api.github.com/repos/{owner}/{repo}/forks"

# Set the headers with the API token for authentication
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Set the fork repo name
data = {
    "name":name
}

# Send a POST request to fork
response = requests.post(url, headers=headers, json=data)

# Check the response status code
if response.ok:
    # Forked successfully
    fork_data = response.json()
    print("Forked successfully!")
    print(fork_data.get('clone_url'))
else:
    # Fork failed
    error_message = response.json().get('message', 'Unknown error')
    error_status = response.status_code
    error_response = json.dumps(response.json(), indent=4)
    print(f"Failed to fork a repo. Error status: {error_status}")
    print(f"Error message: {error_message}")
    print("Error response:")
    print(error_response)

#Code to Clone
try:
    cmd = "git clone {}".format(fork_data.get('clone_url'))
    print("Starting to clone {}".format(fork_data.get('clone_url')))
    print("Running command '{}'".format(cmd))
    os.system(cmd)
    print("Finshed cloning {}".format(fork_data.get('clone_url')))
    print("#####################################")
    print("")
    print("Thank you!")
except:
    print("Error cloning")
# Forked and cloned successfully