#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays the
value of the 'X-Request-Id' variable found in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":

    reqst = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reqst) as response:
        # header_resp = response.getheaders()
        # print(dict(response.headers).get("X-Request-Id"))
        for key, value in response.getheaders():
            if key == 'X-Request-Id':
                print(value)
