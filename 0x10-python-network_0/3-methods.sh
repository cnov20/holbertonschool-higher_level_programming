#!/bin/bash
#Uses curl - dispays all HTTP method a server will accept - given URL
curl -sI --request OPTIONS "$1" | grep Allow | cut -d ' ' -f2-
