import argparse
import os
import subprocess
import requests
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
subprocess.run(['git', 'init', '-b', 'main'])
subprocess.run(['touch', 'README.md'])
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'initial commit'])

payload = {
    "name": name,
    "description": "made with the GitHub API"
}

headers = {
    'Authorization': f'Bearer {GITHUB_API_TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': f'{USERNAME}'
}

response = requests.post(URL, json=payload, headers=headers)

if response.status_code == 201:
    remote_url = response.json()['svn_url']
    subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
    subprocess.run(['git', 'push', 'origin', 'main'])
    print(f"\nREMOTE URL FOR \"{name}\" is: {remote_url}")
else:
    print(f"Failed to create repository. Status Code: {response.status_code}")
    print(f"Reason: {response.text}")
