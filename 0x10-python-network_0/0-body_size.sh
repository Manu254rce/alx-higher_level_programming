#!/bin/bash
# Script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

url=$1
body_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "$body_size"
