#!/bin/bash
# bash script that sends a JSON POST request to a URL, and displays the body of the response.
curl -LsX "$1" POST -H "Content-Type: application/json" -d @$2