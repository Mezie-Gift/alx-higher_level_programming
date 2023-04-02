#!/bin/bash
#This script returns the body of a HTTP reponse
curl -sfL "$1" -X GET
