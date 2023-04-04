#!/usr/bin/python3
"""This script fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.request

reqst = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(reqst) as response:
    body = response.read()

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode("utf-8")))
