#!/usr/bin/python3
"""This script lists 10 commits (from the most recent to oldest) of the \n
              repository “rails” by the user “rails”.
The script that takes 2 arguments in order to solve this challenge:
sys.argv[1]: repository's name (rails).
sys.argv[2]: owner's name (rails).
"""
from sys import argv
import requests

if __name__ == "__main__":
    res = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1])).json()
    if res:
        last_ten = [res[i] for i in range(len(res)-10, len(res))]
        for commits in last_ten:
            print("{}: {}".format(commits.get("sha"), commits.get("commit")
                  .get("author").get("name")))
    else:
        pass
