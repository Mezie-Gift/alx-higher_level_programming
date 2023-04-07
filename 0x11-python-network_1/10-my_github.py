#!/usr/bin/python3
"""This script takes my GitHub credentials (username and password) \n
and uses the GitHub API to display my id.
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    Auth = HTTPBasicAuth(argv[1], argv[2])
    reqst = requests.get(url, auth=Auth)
    if reqst.status_code == 200:
        user_id = reqst.json()['id']
        print(user_id)
    else:
        print("None")
