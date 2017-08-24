#!/bin/bash
#Uses curl - GET request - causes specific response body from server
curl -s --request GET 0.0.0.0:5000/catch_me --data "user_id=98"
