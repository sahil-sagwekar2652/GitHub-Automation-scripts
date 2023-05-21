#!/bin/bash

# GitHub API Token and Username
GITHUB_API_TOKEN="YOUR_GITHUB_API_TOKEN"
USERNAME="YOUR_GITHUB_USERNAME"

# Function to create a new repository
create_repo() {
    local name="$1"
    local description="$2"
    local visibility="$3"

    # Create repository payload
    local payload=$(printf '{"name": "%s", "description": "%s", "private": %s}' "$name" "$description" "$visibility")

    # Send request to create repository
    local response=$(curl -s -H "Authorization: Bearer $GITHUB_API_TOKEN" -H "Content-Type: application/json" -d "$payload" "https://api.github.com/user/repos")

    # Check response status
    local status=$(echo "$response" | jq -r '.message')

    if [[ "$status" != "null" ]]; then
        echo "Error: Repository creation failed - $status"
        exit 1
    else
        echo "Repository '$name' created successfully"
    fi
}

# Check if the required tools are installed
command -v curl >/dev/null 2>&1 || { echo >&2 "Error: curl is not installed. Aborting."; exit 1; }
command -v jq >/dev/null 2>&1 || { echo >&2 "Error: jq is not installed. Aborting."; exit 1; }

# Read repository details from user
read -p "Enter the name for the new repository: " repo_name
read -p "Enter the description for the new repository: " repo_description
read -p "Set the repository visibility (public/private): " repo_visibility

# Validate repository visibility
if [[ "$repo_visibility" != "public" && "$repo_visibility" != "private" ]]; then
    echo "Error: Invalid repository visibility. Allowed values are 'public' or 'private'."
    exit 1
fi

# Create the repository
create_repo "$repo_name" "$repo_description" "$repo_visibility"
