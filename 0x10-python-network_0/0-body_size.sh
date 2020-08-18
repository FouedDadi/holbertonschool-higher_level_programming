#!/bin/bash
# bash script that sends a request and show size of response
curl -sI $1 | grep -i Content-Length | cut -d " " -f2
