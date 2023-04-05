#!/usr/bin/python3
"""This script takes in a URL and an email address, sends a POST request \n
               to the passed URL with the email as a parameter, \n
      and finally displays the body of the response.
"""
from sys import argv
import requests

if __name__ == "__main__":

    email = {"email": argv[2]}
    url = argv[1]
    reqst = requests.post(url, data=email)
    print(reqst.text)
