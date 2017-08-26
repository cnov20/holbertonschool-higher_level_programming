#!/usr/bin/python3

''' This script takes in a string as a parameter from the command line
    - sends GET request to Star Wars API  with passed parameter
    displays body of response as JSON converted to Python dictionary
     manages pagination to display all results - utilizing requests package '''

if __name__ == "__main__":

    import requests
    from sys import argv

    search_param = argv[1]
    url = 'https://swapi.co/api/people/'
    payload = {'search': search_param, 'page': '1'}
    get_req = requests.get(url, params=payload)
    print(get_req.content)
    json_format = get_req.json()
    results = json_format.get('results')
    count = json_format.get('count')
    previous = json_format.get('previous')
    next = json_format.get('next')
    print('Number of result: {}'.format(count))
'''    while (previous is 'null' and next): '''
for item in results:
        name = item.get('name')
        print(name)
