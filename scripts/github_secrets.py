def get_github_secrets():
    """Get the GitHub personal access token and username from the environment."""

    # Get the GitHub personal access token from the environment variable.
    github_api_token = os.environ.get("GITHUB_API_TOKEN")

    # Get the GitHub username from the environment variable.
    username = os.environ.get("USERNAME")

    return github_api_token, username

def main():
    """Get the GitHub personal access token and username and print them to the console."""

    github_api_token, username = get_github_secrets()
    print("GitHub personal access token:", github_api_token)
    print("GitHub username:", username)

if __name__ == "__main__":
    main()
# this is in the reference to the code given in index.html where we see the github_secrets.py code is entirely missing. Its entirely missing from scripts folder too.
