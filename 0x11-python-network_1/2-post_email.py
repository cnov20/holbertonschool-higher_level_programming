#!/usr/bin/python3

''' This script takes in a URL and email from cmd line
    - sends POST request to URL w/ email as parameter and
    displays body of response (utf-8 decoded) '''

if __name__ == "__main__":

    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    email = argv[2]
    header = {'email': email}
    data = urllib.parse.urlencode(header)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data, header)
    with urllib.request.urlopen(req) as response:
        holberton = response.read()
        print(holberton.decode('utf-8', 'strict'))
