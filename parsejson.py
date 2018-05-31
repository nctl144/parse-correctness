import json
import os


# delete generated files if presented
workpath = os.path.join(os.getcwd())

if os.path.exists(os.path.join(workpath, "input-url.txt")):
    os.remove(os.path.join(workpath, "input-url.txt"))

if os.path.exists(os.path.join(workpath, "scheme-url.txt")):
    os.remove(os.path.join(workpath, "scheme-url.txt"))


with open("urltest.json", 'r') as f:
    datastore = json.load(f)

result_url_list = []
scheme_list = []

for item in datastore:
    result_url, scheme = '', ''

    if 'href' in item:
        result_url = item['href']
        scheme = item['protocol']
        scheme = scheme[:-1] if scheme[-1] == ':' else scheme

    # if result_url is not empty -> scheme is not empty
    if result_url.strip() != '':
        result_url_list.append(result_url)
        scheme_list.append(scheme)



url_output_file = open("input-url.txt", "w")
for url in result_url_list:
    url_output_file.write("{0}\n".format(url))
url_output_file.close()

scheme_output_file = open("scheme-url.txt", "w")
for scheme in scheme_list:
    scheme_output_file.write("{0}\n".format(scheme))
scheme_output_file.close()
