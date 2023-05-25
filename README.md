# GitHub Automation Scripts 🤖
![](https://github.com/sahil-sagwekar2652/GitHub-Automation-scripts/workflows/Flake8Linter/badge.svg)

This repository hosts scripts written in bash script and python to automate common Git/GitHub workflows. Normally to connect a local repository to GitHub one has to go to the GitHub website, create a new respository and then add the new GitHub repo as a remote for your local repository. The [create_repo](scripts/create_repo) script automates this process.

[![GitHub-Automation-scripts](https://github-readme-stats.vercel.app/api/pin/?username=sahil-sagwekar2652&repo=GitHub-Automation-scripts&theme=dark)](https://github.com/sahil-sagwekar2652/GitHub-Automation-scripts)<br/>

## Status
<div align="center">
<img src="https://forthebadge.com/images/badges/built-with-love.svg" />
<img src="https://forthebadge.com/images/badges/uses-brains.svg" />
<img src="https://forthebadge.com/images/badges/powered-by-responsibility.svg" />
 <br>
  <img src="https://img.shields.io/github/repo-size/sahil-sagwekar2652/GitHub-Automation-scripts?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues/sahil-sagwekar2652/Github-Automation-scripts?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-closed-raw/sahil-sagwekar2652/Github-Automation-scripts?style=for-the-badge" />
  
  <img src="https://img.shields.io/github/forks/sahil-sagwekar2652/GitHub-Automation-scripts?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr/sahil-sagwekar2652/GitHub-Automation-scripts?style=for-the-badge" />
  <img src="https://img.shields.io/github/issues-pr-closed-raw/sahil-sagwekar2652/GitHub-Automation-scripts?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/sahil-sagwekar2652/GitHub-Automation-scripts?style=for-the-badge" />
  <img src="https://img.shields.io/github/contributors/sahil-sagwekar2652/GitHUb-Automation-scripts?style=for-the-badge" />
  </div>
<br>

## Table of Content
- [Tech](#tech)
- [Installation](#installation)
- [How to use](#how-to-use)
- [Development](#develop)
- [License](#license)

<a name="tech"></a>
## Tech 🖥️
[![My Skills](https://skillicons.dev/icons?i=py,bash,git,github&perline=4)](https://skillicons.dev)


## 🏗️ Installation

## Getting Started

To install and configure the project on your system locally, use the command mentioned below:

```curl https://raw.githubusercontent.com/sahil-sagwekar2652/GitHub-Automation-scripts/main/.setup/install.sh | bash```

## Installation

##### Requirements:
- [Git Bash](https://git-scm.com/downloads) installed on your computer.
- **GitHub personal access token**. (Go to your GitHub profile -> Settings -> Developer settings -> Personal Access Tokens -> Create new token with all the repository permissions)


#### ```Note!!! This script is written exclusively for Git Bash on Windows, you will have to modify it for other shells.```

- ### Step 1:
Fork and clone the repository locally.

- ### Step 2:
Create a ```github_secrets.py``` file in the ./scripts folder and define the following variables inside it.

```py
GITHUB_API_TOKEN = "Your GitHub personal access token"
USERNAME = "Your GitHub username"
```

- ### Step 3:

#### Add the project path to the PATH variable (Recommended)

Run the following command in the project's base directory to add the scripts path to the PATH environment variable.

```sh
$ export PATH=$PATH":"$(pwd)"/scripts"
```

To permanently add the scripts path to the PATH variable, run the below command in the project's root directory. (This file is located in your home directory)  

**Make sure to backup the .bash_profile file elsewhere before making any changes to it.**

```sh
$ echo 'export PATH=$PATH''":'"$(pwd)"'/scripts''"' >> ~/.bash_profile
```

<p style="text-align:center;font-size:1.75rem">OR</p>

#### Run the following commands in the project folder to add the scripts to your bin directory
```sh
$ cp -r /scripts/* /usr/bin/
```

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

<a name="develop"></a>
## 👨‍💻 Development

- Steps to join the project channel on  <a href="https://discord.com/channels/1099745007172329592/1099745007675646042"><img src="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0b5061df29d55a92d945_full_logo_blurple_RGB.svg" width="10%"></a>

    - Go to the [#self-roles](https://discord.com/channels/1099745007172329592/1099745007675646042) channel and choose the 'contributor' and 'GitHub-Automation-scripts' roles.
    - You will be automatically added to the exclusive project channel.
    - It will be the primary channel for all the discussions related to the project.  
  
- Checkout the issues tab to find ideas!

- Want to contribute? Great!  
Make sure to go through the [Contributor's Guide](CONTRIBUTING.md). Trust me it wont take long ;). 


## 🪪 Licence

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](LICENSE)


This project is licensed under the MIT license. For more information, please refer to the LICENSE file.

We hope you find these automation scripts helpful in streamlining your Git and GitHub workflows



## Contributors

<p align="center"
   <a href="https://github.com/sahil-sagwekar2652/GitHub-Automation-scripts/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=sahil-sagwekar2652/GitHub-Automation-scripts" />
</a></p>

