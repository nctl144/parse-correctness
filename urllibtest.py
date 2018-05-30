from urllib.parse import urlparse

import json


with open("urltest.json", 'r') as f:
    datastore = json.load(f)


for item in datastore:
    print(item)
