#!/usr/bin/python3

''' This script takes in a letter as a parameter from the command line
    - sends POST request to specified URL with passed parameter
    displays body of response based on validity of JSON
    returned in body of response - utilizing requests package '''

if __name__ == "__main__":

    import requests
    from sys import argv

    if len(argv) < 2:
        q_param = ""
        print('No result')
    elif not argv[1].isalpha():
        print('No result')
    else:
        q_param = argv[1]
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': q_param}
        post_req = requests.post(url, data=payload)
        json_format = post_req.json()
        if q_param:
            print('[{}] {}'.format(json_format['id'], json_format['name']))
