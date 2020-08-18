#!/bin/bash
# bash script that sends a JSON POST request to a URL, and displays the body of the response.
curl -LsX POST -H  -d "Content-Type: application/json" @"$2" "$1"
