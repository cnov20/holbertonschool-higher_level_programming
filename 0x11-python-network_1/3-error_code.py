#!/usr/bin/python3

''' This script takes in a URL from cmd line
    - sends GET request to URL displays
    body of response (utf-8 decoded)
    - Features HTTP Error handling as exceptions
'''

if __name__ == "__main__":

    import urllib.request
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
