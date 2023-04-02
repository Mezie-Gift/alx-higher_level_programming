#!/bin/bash
#This script deletes an URL passed to it as an argument and displays HTTP response body.
curl -sX DELETE "$1"
