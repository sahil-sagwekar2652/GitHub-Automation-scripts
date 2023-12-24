import argparse
import http.client
import json
import os
import subprocess
from github_secrets import GITHUB_API_TOKEN, USERNAME

def check_environment_variables():
    if not GITHUB_API_TOKEN:
        raise ValueError("Please set the environment variable GITHUB_API_TOKEN in the github_secrets.py file")

def create_local_repository(path, name):
    os.chdir(os.path.join(path, name))
    subprocess.run(['git', 'init', '-b', 'main'], check=True)
    subprocess.run(['touch', 'README.md'], check=True)
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'initial commit'], check=True)

def make_github_api_request(name):
    conn = http.client.HTTPSConnection("api.github.com")
    payload = json.dumps({"name": name, "description": "made with the GitHub API"})
    headers = {'Authorization': f'Bearer {GITHUB_API_TOKEN}', 'Content-Type': 'application/json', 'User-Agent': f'{USERNAME}'}
    conn.request("POST", "/user/repos", payload, headers)
    
    # Check if the request was successful (status code 201)
    res = conn.getresponse()
    if res.status != 201:
        raise RuntimeError(f"Failed to create repository. Status code: {res.status}")

    data = res.read().decode("utf-8")
    response = json.loads(data)
    return response['svn_url']

def main():
    check_environment_variables()

    parser = argparse.ArgumentParser(description='creates a local repository linked with a remote repository')
    parser.add_argument('path', metavar='PATH', type=str, help='Enter the path for the new repository')
    parser.add_argument('name', metavar='NAME', type=str, help='Enter a name for the new repository')
    args = parser.parse_args()

    name = args.name
    path = args.path

    create_local_repository(path, name)
    remote_url = make_github_api_request(name)

    subprocess.run(['git', 'remote', 'add', 'origin', remote_url])
    subprocess.run(['git', 'push', 'origin', 'main'])

    print(f"\nREMOTE URL FOR \"{name}\" is: {remote_url}")

if __name__ == "__main__":
    main()
