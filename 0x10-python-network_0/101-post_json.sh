#!/bin/bash
#Uses curl - POST request - contents of JSON file - to URL passed as argument / filename as second argument - displays body of response
curl -s --request POST "$1" --header "Content-Type:application/json" --data "@$2"
