#!/bin/bash
#This script displays the `Content_Length` of an HTTP request
response=$(curl -sI "$1$2") && content_length=$(echo "$response" | grep -i content-length | awk '{print $2}') && echo "$content_length"
