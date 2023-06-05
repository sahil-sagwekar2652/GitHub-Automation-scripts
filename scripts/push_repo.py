#!/usr/bin/env python

import argparse
import os
from github_secrets import GITHUB_API_TOKEN


def parseArgs():
    parser = argparse.ArgumentParser(description='Push an existing local repository to a newly created remote repository of the same name')  # noqa: E501
    parser.add_argument('path',
                        metavar='PATH',
                        type=str,
                        help='Enter the path for existing local repository')
    parser.add_argument('url',
                        metavar='URL',
                        type=str,
                        help='Enter the newly created remote repository url (.git)')
    parser.add_argument('description',
                        metavar='DESCRIPTION',
                        type=str,
                        help='Enter the description for remote repository')
    args = parser.parse_args()
    return args


def pushRepo(remote_url):
    origin = remote_url[:8] + GITHUB_API_TOKEN + "@" + remote_url[8:]
    os.system(f'git push {origin} --mirror')


def main():
    path = args.path
    remote_url = args.url

    os.chdir(path)
    if os.path.isdir('./.git') is False:
        print("Not in a git directory")
        exit()

    pushRepo(remote_url)


if __name__ == "__main__":
    args = parseArgs()
    main()
