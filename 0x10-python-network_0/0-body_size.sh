#!/bin/bash
#Sends a 'curl' cmd  request to a given URL and displays size of response body
curl -s -o /dev/null 0.0.0.0:5000 --write-out '%{size_download}\n'
