#!/bin/bash
#Sends a 'curl' cmd  request to a given URL and displays size of response body
curl -sI 0.0.0.0:5000 | grep Content-Length | cut -d ' ' -f2
