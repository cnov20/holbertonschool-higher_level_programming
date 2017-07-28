#!/bin/bash
#Uses curl - GET request - sends extra header variable in request - displays body of response
curl -sH 'X-HolbertonSchool-User-Id: 98' "$1"
