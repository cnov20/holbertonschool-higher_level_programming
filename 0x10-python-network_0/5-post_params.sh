#!/bin/bash
#Uses curl - POST request - sends extra header variables in request - displays body of response
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
