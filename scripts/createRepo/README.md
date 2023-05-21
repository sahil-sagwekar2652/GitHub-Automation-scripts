### GitHub Repository Creation Script

This bash script allows you to create a new repository on GitHub. It interacts with the GitHub API to create the repository and handles exceptions gracefully.

#### Prerequisites

Before running the script, ensure that you have the following requirements:

- `curl` command-line tool
- `jq` command-line tool

If you don't have these tools installed, you can install them using the package manager available for your operating system.

#### Installation

1. Download the script file `create_repo.sh` to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Make the script file executable by running the following command:

   ```bash
   chmod +x create_repo.sh
#### Usage
1. Open a terminal and navigate to the directory where the script is located.

2. Run the following command to execute the script:
  ```bash
 ./create_repo.sh

3. The script will prompt you to enter the repository details:

   - Repository Name: Enter a name for the new repository.
   - Repository Description: Provide a description for the new     repository.
   - Repository Visibility: Set the visibility of the repository (public/private).
   - After providing the required details, the script will create the repository on GitHub using the provided information.

5. If the repository is created successfully, you will see a success message indicating that the repository was created.
 ```
 Repository 'your-repo-name' created successfully
 ```

If there is any error during the repository creation process, an appropriate error message will be displayed.

GitHub API Token
To authenticate with the GitHub API and create repositories, you need to provide your GitHub API token. Make sure to update the GITHUB_API_TOKEN variable in the create_repo.sh script file with your actual GitHub API token. This token should have the necessary permissions to create repositories on your account.