#!/bin/bash
# bash script that sends a GET request to the URL, and displays the body of the response
curl -LsX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
