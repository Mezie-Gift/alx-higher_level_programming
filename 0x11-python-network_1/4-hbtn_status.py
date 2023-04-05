#!/usr/bin/python3
"""This script fetches `https://alx-intranet.hbtn.io/status`\n
using `request` package.
"""
import requests


r = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
