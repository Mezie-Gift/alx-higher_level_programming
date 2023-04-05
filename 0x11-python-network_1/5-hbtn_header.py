#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays the \n
                 value of the variable X-Request-Id in the response header.
"""
from sys import argv
import requests

request = requests.get(argv[1])
header = request.headers['X-Request-Id']
print(header)
