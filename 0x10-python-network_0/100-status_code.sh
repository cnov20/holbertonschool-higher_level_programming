#!/bin/bash
#Uses curl - GET request - to URL passed as argument - displays only STATUS code of esponse
curl -s -o /dev/null "$1" --write-out '%{http_code}'
