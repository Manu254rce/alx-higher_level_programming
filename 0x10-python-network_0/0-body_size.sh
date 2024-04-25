#!/bin/bash
# Script that takes in a URL, sends a request to that URL displaying the size
url=$1
body_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "$body_size"
