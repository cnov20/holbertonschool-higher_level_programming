#!/usr/bin/python3

''' This script takes in a URL from cmd line - sends reuest to URL
    and displays value of specific variabled found in header of response
    using requests package '''

if __name__ == "__main__":

    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    headers = req.headers
    x_request_id = headers['X-Request-Id']
    print(x_request_id)
