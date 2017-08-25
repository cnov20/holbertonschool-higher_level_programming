#!/usr/bin/python3

''' This script takes in a URL from cmd line - sends reuest to URL
    and displays value of specific variabled found in header of response '''

if __name__ == "__main__":

    import urllib.request
    from sys import argv

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        holberton = dict(response.info())
        for k, v in holberton.items():
            if k == 'X-Request-Id':
                print(v)
