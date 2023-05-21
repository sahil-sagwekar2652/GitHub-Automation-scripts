## Push Repo Script

This script automates the process of pushing an existing local repository to a remote repository on GitHub using the GitHub API.

### Installation

1. Make sure you have Python installed on your system. You can download and install Python from the official Python website: [python.org](https://www.python.org/).

2. Clone or download the repository containing the push repo script to your local machine.

3. Navigate to the project directory in your command-line interface.

4. Install the required packages by running the following command:

   ```bash
   pip install -r requirements.txt
   ```
This will install the necessary PyGithub package.

5. Set up your GitHub API token:

   - Create a file named github_secrets.py in the project directory.

   - Open github_secrets.py and add the following lines:

      ```python
        GITHUB_API_TOKEN = "YOUR_GITHUB_API_TOKEN"
      ```
      
     Replace GITHUB_API_TOKEN with your actual GitHub API token.

     Note: Ensure that your GitHub API token has the required permissions to create repositories.
# Usage
To run the push repo script, follow these steps:

1. Open a command-line interface.

2. Navigate to the project directory where the push_repo.py script is located.

3. Run the script using the following command:
   ```
     python push_repo.py <path_to_local_repo> <name_of_remote_repo>
   ```
   
   Replace <path_to_local_repo> with the path to your existing local repository and <name_of_remote_repo> with the desired name for the remote repository on GitHub.

   For example:
   ```
   python push_repo.py /path/to/local/repo my-remote-repo
   ```
The script will initiate and push your existing local repository to a new remote repository on GitHub.

Note: Ensure that you have a valid GitHub access token set in the GITHUB_API_TOKEN environment variable or in the github_secrets.py file for authentication with the GitHub API.

