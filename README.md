# GitHub Automation Scripts 🤖

This repository hosts scripts written in bash script and python to automate common Git/GitHub workflows. Normally to connect a local repository to GitHub one has to go to the GitHub website, create a new respository and then add the new GitHub repo as a remote for your local repository. The [create_repo](scripts/create_repo) script automates this process.

[![GitHub-Automation-scripts](https://github-readme-stats.vercel.app/api/pin/?username=sahil-sagwekar2652&repo=GitHub-Automation-scripts&theme=dark)](https://github.com/sahil-sagwekar2652/GitHub-Automation-scripts)<br/>


## Tech 🖥️
[![My Skills](https://skillicons.dev/icons?i=py,bash,git,github&perline=4)](https://skillicons.dev)

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
Make sure to go through the [Contributor's Guide](CONTRIBUTING.md).


## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](LICENSE)
