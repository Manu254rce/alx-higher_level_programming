#!/bin/bash
# Script that takes in a URL, sends a request to that URL displaying the size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r'
