#!/bin/bash
# bash script that sends a request and displays only the status code of the response.
curl -o "$1"/dev/null -s -w "%{http_code}\n" "$1"
