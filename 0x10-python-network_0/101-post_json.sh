#!/bin/bash
# bash script that sends a JSON POST request to a URL, and displays the body of the response.
curl -LsX POST -H "Content-Type: application/json" -d @"$2" "$1"
