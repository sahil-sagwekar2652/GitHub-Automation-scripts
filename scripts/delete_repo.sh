import github_secrets

def delete_repository(repo_name):
    api_key = github_secrets.API_KEY
    auth_header = "Authorization: token {}".format(api_key)
    response = curl -X DELETE -s -H "{} " "https://api.github.com/repos/{}/".format(auth_header, repo_name)

    # Check the response status code
    if response -ne 202:
        # The response status code is not 202, which means the deletion failed.
        # Check the response body for the error message.
        error_message = echo response | jq -r '.message'
        echo "An error occurred while deleting the repository."
        echo "Response: $response"
        echo "Error message: $error_message"
        exit 1

    # The repository was deleted successfully.
    echo "Repository '$repo_name' successfully deleted."

if __name__ == "__main__":
    repo_name = read -p "Enter the name of the repository to delete: "
    delete_repository(repo_name)



