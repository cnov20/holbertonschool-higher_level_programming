#!/usr/bin/python3

''' This script takes in a string as a parameter from the command line
    - sends GET request to Star Wars API  with passed parameter
    displays body of response as JSON converted to Python dictionary
     - utilizing requests package '''

if __name__ == "__main__":

    import requests
    from sys import argv

    search_param = argv[1]
    url = 'https://swapi.co/api/people/'
    payload = {'search': search_param}
    get_req = requests.get(url, params=payload)
    json_format = get_req.json()
    results = json_format.get('results')
    num_results = 0
    names = ""
    for item in results:
        num_results += 1
        name = item.get('name')
        names += name + '\n'
    print('Number of result: {}'.format(num_results))
    print(names)
