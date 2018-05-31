from urllib.parse import urlparse, urljoin

import json
import collections


with open("urltest.json", 'r') as f:
    datastore = json.load(f)

incorrect_url = collections.defaultdict(list)

for item in datastore:
    input_url = item['input']
    base_url = item['base']

    if base_url == 'about:blank':
        base_url = ''

    scheme, netloc, path, search, failure, result_url = '', '', '', '', False, ''

    if 'href' in item:
        result_url = item['href']
        result_url = result_url[:-1] if result_url[-1] == '/' else result_url

    if 'protocol' in item:
        scheme = item['protocol']
        scheme = scheme[:-1] if scheme[-1] == ':' else scheme

    if 'hostname' in item:
        netloc = item['hostname']

    if 'pathname' in item:
        path = item['pathname']

    if 'search' in item:
        query = item['search']

    if 'failure' in item:
        failure = True

    try:
        join_url = urljoin(base_url, input_url)
        if len(join_url) > 1:
            join_url = join_url[:-1] if join_url[-1] == '/' else join_url


        if result_url.lower() != '' and result_url.lower() != join_url.lower():
            if not failure:
                incorrect_url[input_url].append("incorrect join url")


        parsed_obj = urlparse(join_url)

        if scheme.lower() != '' and parsed_obj.scheme.lower() != scheme.lower():
            if not failure:
                incorrect_url[input_url].append("incorrect scheme")

        if netloc.lower() != '' and parsed_obj.netloc.lower() != netloc.lower():
            if not failure:
                incorrect_url[input_url].append("incorrect netloc")


    except ValueError:
        if not failure:
            print("the value error url is:", input_url)



for key, val in incorrect_url.items():
    print(key, '----', val)
