#!/bin/bash

# Prompt the user to enter the repository name
read -p "Enter the name of the repository to delete: " repo_name

# Check if the repo name is empty
if [[ -z $repo_name ]]; then
  echo "Please enter a repository name."
  exit 1
fi

# Prompt for confirmation
read -p "Are you sure you want to delete the repository '$repo_name'? This action cannot be undone. (y/n): " confirm

# Convert the confirmation input to lowercase
confirm=${confirm,,}

# Check if the user confirmed the deletion
if [[ $confirm != "y" ]]; then
  echo "Repository deletion canceled."
  exit 0
fi

# Authenticate the user using personal access token (PAT)
# Replace <PAT> with your actual personal access token
auth_header="Authorization: token <PAT>"

# Delete the repository using the GitHub API
response=$(curl -X DELETE -s -H "$auth_header" "https://api.github.com/repos/$repo_name")

# Check the response status code
if [[ $response -ne 202 ]]; then
  # The response status code is not 202, which means the deletion failed.
  # Check the response body for the error message.
  error_message=$(echo "$response" | jq -r '.message')
  echo "An error occurred while deleting the repository."
  echo "Error message: $error_message"
  exit 1
fi

# The repository was deleted successfully.
echo "Repository '$repo_name' successfully deleted."


