# GitHub Automation Scripts

This repository hosts scripts written in bash script and python to automate common Git/GitHub workflows. Normally to connect a local repository to GitHub one has to go to the GitHub website, create a new respository and then add the new GitHub repo as a remote for your local repository. The [create_repo](scripts/create_repo) script automates this process.

## Tech
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## Installation
##### Requirements:
- [Git Bash](https://git-scm.com/downloads) installed on your computer.
- **GitHub personal access token**. (Go to your GitHub profile -> Settings -> Developer settings -> Personal Access Tokens -> Create new token with all the repo permissions)
- You will need to set an environment variable 'GITHUB_API_TOKEN' for Git Bash.

###### Note!!! This script is written exclusively for Git Bash on Windows, you will have to modify it for other shells.

##### Run the following commands in the project folder to add the scripts to your bin directory
```sh
$ cp -r /scripts/* /usr/bin/
$ export GITHUB_API_TOKEN=your_github_personal_access_token
```
- Add the "export GITHUB_API_TOKEN=your_github_personal_access_token" to your ~/.bash_profile to permanently set the environment variable

## How to use
After the installation is complete then the 'create_repo' command should execute in any directory.

- Run the command with a '-h' flag to see the help menu
```sh
create_repo -h
```
- Sample usage
```sh
create_repo <PATH_NAME> <REPO_NAME>
```
- <PATH_NAME> is the path where you want to create the local repository and <REPO_NAME> is the name for your repo
- Example:
```sh
create_repo . test-repo
```
The result is a local respository is created with a connected remote repository automatically!


## Development
Want to contribute? Great!
Read this first -> [Contributor's Guide](CONTRIBUTING.md)


## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](LICENSE)
