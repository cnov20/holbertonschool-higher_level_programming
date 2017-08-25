#!/usr/bin/python3

''' This script takes in a URL and email from cmd line
    - sends POST request to URL w/ email as parameter and
    displays body of response (utf-8 decoded) - utilizing requests package '''

if __name__ == "__main__":

    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(url)
    status_code = req.status_code
    if status_code == requests.codes.ok:
        print(req.content.decode('utf-8'))
    elif status_code >= 400:
        print('Error code: {}'.format(status_code))
    else:
        print(status_code)
