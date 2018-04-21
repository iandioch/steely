import json

from steely import config

import requests

API_KEY = config.TMDB_KEY

SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'

def search(s):
    params = {
        'api_key': API_KEY,
        'query': s
    }
    print(params)
    data = requests.get(url=SEARCH_URL, params=params).json()
    print(data)

if __name__ == '__main__':
    print(search('what happens in vegas'))
