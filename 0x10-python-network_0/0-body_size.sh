#!/usr/bin/env bash
#Takes in a URL, sends a request to it, and displays the
#+size of the body of the response.

response=$(curl -sI "$1$2")
content_length=$(echo "$response" | grep -i content-length | awk '{print $2}')
echo "$content_length"
