#!/usr/bin/env python

'''
This script is used to create a local repository linked with a remote repository.
'''

# Imports the required modules
import argparse  # required for parsing the command line arguments passed to the script
import os  # required for creating the directory and changing the directory and running the git commands # noqa: E501
import http.client  # required for making the http request
import json  # required for parsing the response received from the http request
from github_secrets import GITHUB_API_TOKEN, USERNAME  # required for authenticating the http request and setting the user agent # noqa: E501


# Checks if the environment variables are set or not. If not, raises an error as ValueError.  # noqa: E501
# Environment variables are set in the github_secrets.py file which contains the GITHUB_API_TOKEN and USERNAME # noqa: E501
# The GITHUB_API_TOKEN is the personal access token generated from the GitHub account. # noqa: E501
if not GITHUB_API_TOKEN:
    raise ValueError("Please set the environment variable GITHUB_API_TOKEN in the github_secrets.py file")  # noqa: E501

# Base URL for the GitHub API which is used to create a new repository # noqa: E501
URL = "https://api.github.com/user/repos"

# Creates a parser object of the argparse class
# The parser object is used to parse the command line arguments passed to the script # noqa: E501
# The parser object is used to create the help text for the script # noqa: E501
parser = argparse.ArgumentParser(description='creates a local repository linked with a remote repository')  # noqa: E501

# Adds the arguments to the parser object
parser.add_argument('path',  # This argument can be accessed using the `path` variable # noqa: E501
                    metavar='PATH',
                    type=str,
                    help='Enter the path for the new repository')
parser.add_argument('name',  # This argument can be accessed using the `name` variable # noqa: E501
                    metavar='NAME',
                    type=str,
                    help='Enter a name for the new repository')
args = parser.parse_args()  # parses the arguments passed to the script. The arguments are stored in the `args` variable # noqa: E501

name = args.name  # stores the name of the repository from `args` in the name variable
path = args.path  # stores the path of the repository from `args` in the path variable


# The following codes creates a new directory with the name of the repository and initializes it with git using the `os` module # noqa: E501
os.chdir(path)  # changes the directory to the path specified in the `path` variable # noqa: E501
os.mkdir(name)  # creates a new directory with the name specified in the `name` variable # noqa: E501
os.chdir(name)  # changes the directory to the newly created directory # noqa: E501
os.system('git init -b main')  # This executes 'git init -b main' as a system command as if it were written in git bash. It initializes the directory with git and sets the default branch to `main` # noqa: E501
os.system('touch README.md')  # creates a README.md file # noqa: E501
os.system('git add . && git commit -m "initial commit"')  # adds the newly created README.md file to the staging area and commits it with the message# noqa: E501


# The following code makes a POST request to the GitHub API to create a new repository # noqa: E501
conn = http.client.HTTPSConnection("api.github.com")  # creates a connection object
# The payload is the data that is sent
payload = json.dumps({
    "name": name,
    "description": "made with the GitHub API"
})

# Metadata that is sent along with the request
# The metadata contains the authorization token, the content type and the user agent # noqa: E501
headers = {
    'Authorization': f'Bearer {GITHUB_API_TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': f'{USERNAME}'
}

# The request is made to the URL with the payload and the headers
# The response received is stored in the `res` variable
# The response is read and decoded using utf-8 encoding and stored in the `data` variable
# The `data` variable is parsed using the json module and stored in the `response` variable # noqa: E501
# The `response` variable contains the response received from the GitHub API, which is a JSON object # noqa: E501
conn.request("POST", "/user/repos", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
response = json.loads(data)

print(response)
remote_url = response['svn_url']  # stores the remoteurl using the key `svn_url` in the `response` variable # noqa: E501

# Runs the git commands as system commands # noqa: E501
os.system(f'git remote add origin {remote_url}')  # adds the remote url to the local repository
os.system('git push origin main')  # Pushes the local repository to the remote repository
print(f"\nREMOTE URL FOR \"{name}\" is: {remote_url}")  # Prints the remote url
