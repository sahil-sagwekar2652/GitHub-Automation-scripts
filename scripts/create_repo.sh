#!/bin/bash

# GitHub Personal Access Token
TOKEN="YOUR_PERSONAL_ACCESS_TOKEN"

# Repository name
REPO_NAME="new-repo"

# Repository description
REPO_DESCRIPTION="This is a new repository"

# API endpoint
API_URL="https://api.github.com/user/repos"

# Create repository payload
PAYLOAD=$(cat << EOF
{
  "name": "$REPO_NAME",
  "description": "$REPO_DESCRIPTION",
  "private": false,
  "auto_init": false
}
EOF
)

# Send POST request to create repository
response=$(curl -s -H "Authorization: token $TOKEN" -d "$PAYLOAD" "$API_URL")

# Check response status
if [[ "$(echo "$response" | jq -r '.message')" == "Validation Failed" ]]; then
  echo "Error: Failed to create repository."
  echo "Reason: $(echo "$response" | jq -r '.errors[0].message')"
else
  echo "Repository '$REPO_NAME' created successfully."
fi
