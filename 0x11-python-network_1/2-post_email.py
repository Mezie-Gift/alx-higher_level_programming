#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST request to the \n
             passed URL with the email as a parameter, and displays \n
          the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
post_data = {'email': sys.argv[2]}
email = urllib.parse.urlencode(post_data)
email = email.encode('ascii')

reqst = urllib.request.Request(url, data=email, method='post')
with urllib.request.urlopen(reqst) as response:
    post_response = response.read().decode('utf-8')
    print(post_response)
