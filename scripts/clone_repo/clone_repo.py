import argparse
import os
import http.client
import json
from github_secrets import GITHUB_API_TOKEN, USERNAME

if not GITHUB_API_TOKEN:
    raise ValueError("Please set the environment variable GITHUB_API_TOKEN in the github_secrets.py file")  # noqa: E501

URL = "https://api.github.com/user/repos"

parser = argparse.ArgumentParser(description='clones an existing remote repository to a local environment')  # noqa: E501

parser.add_argument('owner',
                    metavar='OWNER',
                    type=str,
                    help='Enter the owner/username of the remote repository')
parser.add_argument('repo',
                    metavar='REPO',
                    type=str,
                    help='Enter the name of the remote repository')
parser.add_argument('path',
                    metavar='PATH',
                    type=str,
                    help='Enter the path where you want to clone the repository')
args = parser.parse_args()

owner = args.owner
repo = args.repo
path = args.path

os.chdir(path)

conn = http.client.HTTPSConnection("api.github.com")
headers = {
    'Authorization': f'Bearer {GITHUB_API_TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': f'{USERNAME}'
}

conn.request("GET", f"/repos/{owner}/{repo}", headers=headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
response = json.loads(data)

if 'message' in response:
    print(f"Error: {response['message']}")
else:
    clone_url = response['clone_url']
    os.system(f"git clone {clone_url}")

print("Cloning complete!")
