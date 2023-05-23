#!/usr/bin/env python

import argparse
import os
import http.client
import json
from github_secrets import GITHUB_API_TOKEN, USERNAME

if not GITHUB_API_TOKEN:
    raise ValueError("Please set the environment variable GITHUB_API_TOKEN in the github_secrets.py file")  # noqa: E501

URL = "https://api.github.com/user/repos"

parser = argparse.ArgumentParser(description='creates a local repository linked with a remote repository')  # noqa: E501

parser.add_argument('path',
                    metavar='PATH',
                    type=str,
                    help='Enter the path for the new repository')
parser.add_argument('name',
                    metavar='NAME',
                    type=str,
                    help='Enter a name for the new repository')
args = parser.parse_args()

name = args.name
path = args.path

os.chdir(path)
os.mkdir(name)
os.chdir(name)
os.system('git init -b main')
os.system('touch README.md')
os.system('git add . && git commit -m "initial commit"')
# os.system('git status')

conn = http.client.HTTPSConnection("api.github.com")
payload = json.dumps({
    "name": name,
    "description": "made with the GitHub API"
})
headers = {
    'Authorization': f'Bearer {GITHUB_API_TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': f'{USERNAME}'
}

conn.request("POST", "/user/repos", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
response = json.loads(data)

print(response)
remote_url = response['svn_url']

os.system(f'git remote add origin {remote_url}')
os.system('git push origin main')
print(f"\nREMOTE URL FOR \"{name}\" is: {remote_url}")
