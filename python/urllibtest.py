from urllib.parse import urlparse, urljoin

import json
import collections

def read_data(filename, arr):
    with open(filename, 'r') as f:
        for item in f:
            if item[-1:] == '\n':
                item = item.replace('\n', '')
            arr.append(item)

def main():

    input_list, scheme_list, netloc_list, path_list = [], [], [], []

    read_data("input-url.txt", input_list)
    read_data("scheme-url.txt", scheme_list)
    read_data("netloc-url.txt", netloc_list)
    read_data("path-url.txt", path_list)

    counter = 0

    for url in input_list:
        parsed_result = urlparse(url)
        path_result = parsed_result.path
        if parsed_result.params != "":
            path_result = parsed_result.path + ";" + parsed_result.params

        if scheme_list[counter] != parsed_result.scheme:
            print("unmatched scheme at", url)

        if netloc_list[counter] != parsed_result.netloc:
            print("unmatched netloc at", url)

        if path_result != path_list[counter]:
            if ((path_result == "" and path_list[counter] == '/') or (path_result == "/" and path_list[counter] == "")):
                pass
            else:
                print("unmatched path at", url)

        counter += 1


if __name__ == "__main__":
    main()
