#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to \n
    `http://0.0.0.0:5000/search_user` with the letter as a parameter.
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 1:
        q = ""
    else:
        argv[1].isalpha()
        load = {"q": argv[1]}
    reqst = requests.post(url, data=load)
    try:
        response = reqst.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
