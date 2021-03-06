#!/usr/bin/python3

"""
    opensearch.py

    MediaWiki Action API Code Samples
    Demo of `Opensearch` module: Search the wiki and obtain
    results in an OpenSearch (http://www.opensearch.org) format
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

SEARCHTERM = "Hampi"

PARAMS = {
    'action':"opensearch",
    'search':SEARCHTERM,
    'limit': 5,
    'namespace':0,
    'format':"json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
