import requests
import subprocess

def fork_and_clone_repo(username, repository, access_token):
    # Fork the repository using GitHub API
    fork_url = f"https://api.github.com/repos/{username}/{repository}/forks"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.post(fork_url, headers=headers)

    if response.status_code == 202:
        forked_repo_name = response.json()["name"]
        clone_url = f"https://github.com/{username}/{forked_repo_name}.git"
        
        # Clone the forked repository using git
        subprocess.run(["git", "clone", clone_url])
        print("Fork and clone completed successfully.")
    else:
        print("Forking the repository failed. Please check your access token and repository details.")

# Usage example
username = "original-username"
repository = "original-repo"
access_token = "YOUR_GITHUB_ACCESS_TOKEN"

fork_and_clone_repo(username, repository, access_token)
