#!/usr/bin/python3

''' This script takes in Github credentials from the cmd line
    - sends GET request to Github API with passed parameters
    displays body of response - Github id - utilizing requests package '''

if __name__ == "__main__":

    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    get_req = requests.get(url, auth=(username, password))
    json_format = get_req.json()
    id = json_format.get('id')
    print(id)
