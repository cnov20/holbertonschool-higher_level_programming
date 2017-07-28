#!/bin/bash
#Uses curl - POST request - contents of JSON file - to URL passed as argument
curl -s --request POST "$1" --header "Content-Type:application/json" --data "@$2"
