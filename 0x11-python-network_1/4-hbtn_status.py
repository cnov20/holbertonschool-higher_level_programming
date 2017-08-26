#!/usr/bin/python3

''' This script fetches a URL - displays body of response
    in specific format '''

if __name__ == "__main__":

    import requests
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url)
    content = req.content
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content.decode('utf-8')))
