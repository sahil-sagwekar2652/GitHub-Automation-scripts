#!/bin/bash

# Set your GitHub access token and repository details
TOKEN="YOUR_GITHUB_ACCESS_TOKEN"
REPO_OWNER="OWNER"
REPO_NAME="REPO_NAME"
BASE_BRANCH="base_branch"  # The branch you want to merge into
HEAD_BRANCH="head_branch"  # The branch you want to merge from
PR_TITLE="Pull Request Title"
PR_BODY="Pull Request Body"

# Method 1: Using GitHub API with cURL
create_pull_request_with_curl() {
  # Create a pull request using GitHub API
  pull_request=$(curl -X POST -H "Authorization: token $TOKEN" \
      -d '{"title": "'"$PR_TITLE"'", "body": "'"$PR_BODY"'", "head": "'"$REPO_OWNER:$HEAD_BRANCH"'", "base": "'"$BASE_BRANCH"'"}' \
      "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls")

  # Extract the pull request number from the response
  pr_number=$(echo "$pull_request" | jq -r '.number')

  # Check if the pull request was successfully created
  if [ -n "$pr_number" ] && [ "$pr_number" != "null" ]; then
      echo "Pull request created successfully using cURL. PR Number: $pr_number"
  else
      echo "Failed to create pull request using cURL. Error message:"
      echo "$pull_request" | jq -r '.message'
  fi
}

# Method 2: Using hub command-line tool
create_pull_request_with_hub() {
  # Install hub if not already installed
  if ! command -v hub &> /dev/null; then
      echo "hub command-line tool is not installed. Installing..."
      sudo apt-get update
      sudo apt-get install hub -y
  fi

  # Create a pull request using hub
  hub pull-request -b "$REPO_OWNER:$BASE_BRANCH" -h "$REPO_OWNER:$HEAD_BRANCH" -m "$PR_TITLE" -m "$PR_BODY"
}

# Method 3: Using gh command-line tool
create_pull_request_with_gh() {
  # Install gh if not already installed
  if ! command -v gh &> /dev/null; then
      echo "gh command-line tool is not installed. Installing..."
      sudo apt-get update
      sudo apt-get install gh -y
  fi

  # Create a pull request using gh
  gh pr create --base "$BASE_BRANCH" --head "$HEAD_BRANCH" --title "$PR_TITLE" --body "$PR_BODY"
}

# Execute the desired method to create a pull request
# Uncomment the method you want to use, and comment out the others

# Method 1: Using GitHub API with cURL
# create_pull_request_with_curl

# Method 2: Using hub command-line tool
# create_pull_request_with_hub

# Method 3: Using gh command-line tool
# create_pull_request_with_gh
