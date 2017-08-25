#!/usr/bin/python3

''' This script takes in a URL and email from cmd line
    - sends POST request to URL w/ email as parameter and
    displays body of response (utf-8 decoded) - utilizing requests package '''

if __name__ == "__main__":

    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]
    header = {'email': email}
    post_req = requests.post(url, header)
    content = post_req.content
    print(content.decode('utf-8'))
