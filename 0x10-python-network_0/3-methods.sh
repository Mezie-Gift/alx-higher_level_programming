#!/bin/bash
#This script takes in an URL and displays all the HTTP methods the server would accept.
options=$(curl -sI OPTIONS "$1") && allowed_methods=$(echo "$options" | grep "Allow:" | sed 's/Allow: //') && echo "$allowed_methods"
