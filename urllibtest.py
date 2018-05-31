from urllib.parse import urlparse, urljoin

import json
import collections


with open("urltest.json", 'r') as f:
    datastore = json.load(f)

incorrect_url = collections.defaultdict(list)

for item in datastore:
    input_url = item['input']
    base_url = item['base']

    scheme, netloc, path, search, failure, result_url = '', '', '', '', False, ''

    if 'href' in item:
        result_url = item['href']
    if 'protocol' in item:
        scheme = item['protocol']

    if 'hostname' in item:
        netloc = item['hostname']

    if 'pathname' in item:
        path = item['pathname']

    if 'search' in item:
        query = item['search']

    if 'failure' in item:
        failure = True

    try:
        parsed_obj = urlparse(input_url)

        if scheme != '' and parsed_obj.scheme + ":" != scheme:
            if not failure:
                incorrect_url[input_url].append("incorrect scheme")

        # check the join result
        join_url = urljoin(base_url, input_url)

        if result_url != '' and result_url != join_url:
            if not failure:
                incorrect_url[input_url].append("incorrect join url")



    except ValueError:
        if not failure:
            print("the value error url is:", input_url)



for key, val in incorrect_url.items():
    print(key, '----', val)
