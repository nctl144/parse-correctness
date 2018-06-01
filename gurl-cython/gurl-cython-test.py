from pygurl import URL

import json
import collections

def read_data(filename, arr):
    with open(filename, 'r') as f:
        for item in f:
            if item[-1:] == '\n':
                item = item.replace('\n', '')
            arr.append(item)

def main():

    input_list, scheme_list, netloc_list = [], [], []

    read_data("input-url.txt", input_list)
    read_data("scheme-url.txt", scheme_list)
    read_data("netloc-url.txt", netloc_list)

    counter = 0

    for url in input_list:
        parsed_result = URL(url.encode())

        if scheme_list[counter] != parsed_result.scheme().decode():
            print("unmatched scheme at", url)

        if netloc_list[counter] != parsed_result.host().decode():
            print("unmatched netloc at", url)

        counter += 1


if __name__ == "__main__":
    main()
