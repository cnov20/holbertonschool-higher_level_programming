#!/bin/bash
#Uses curl - dispays all HTTP method a server will accept - given URL
curl -si --request OPTIONS "$1" | grep Allow | cut -d ' ' -f2-4
