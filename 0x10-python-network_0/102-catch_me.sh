#!/bin/bash
#Uses curl - GET request - causes specific response body from server
curl -sL --header 'Origin:HolbertonSchool' --request PUT 0.0.0.0:5000/catch_me --data "user_id=98"
