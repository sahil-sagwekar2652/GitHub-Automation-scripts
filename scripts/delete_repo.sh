#!/bin/bash

# Prompt the user to enter the repository name
read -p "Enter the name of the repository to delete: " repo_name

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
if [[ $(echo "$response" | jq -r '.message') == "Not Found" ]]; then
  echo "Repository '$repo_name' not found."
elif [[ $(echo "$response" | jq -r '.message') == "Bad credentials" ]]; then
  echo "Authentication failed. Please check your credentials."
elif [[ $(echo "$response" | jq -r '.message') == "Repository marked for deletion." ]]; then
  echo "Repository '$repo_name' successfully deleted."
else
  echo "An error occurred while deleting the repository."
  echo "Response: $response"
fi
