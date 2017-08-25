#!/usr/bin/python3

''' This script fetches the body of an http request
    and displays it in a specific format '''

if __name__ == "__main__":

    import urllib.request

    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        holberton = response.read()
        print('Body response:')
        print('\t - type: {}'.format(type(holberton)))
        print('\t - content: {}'.format(holberton))
        print('\t - utf8 content: {}'.format(holberton.
                                             decode('utf-8', 'strict')))
