#!/bin/bash
#This script takes in an URL and displays all the HTTP methods the server would accept.
curl -sX OPTIONS "$1"
