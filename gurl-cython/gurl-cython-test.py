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

    input_list, scheme_list, netloc_list, path_list = [], [], [], []

    read_data("input-url.txt", input_list)
    read_data("scheme-url.txt", scheme_list)
    read_data("netloc-url.txt", netloc_list)
    read_data("path-url.txt", path_list)

    counter_scheme = 0
    counter_netloc = 0
    counter_path = 0

    for url in input_list:
        parsed_result = URL(url.encode())
        scheme_result = parsed_result.scheme().decode()

        if scheme_list[counter_scheme] != scheme_result:
            print("unmatched scheme at", url)

        counter_scheme += 1

    print('\n')

    # for url in input_list:
    #     parsed_result = URL(url.encode())
    #     netloc_result = parsed_result.host().decode()
    #
    #     if netloc_list[counter_netloc] != netloc_result:
    #         print("unmatched netloc at", url, "the result is", netloc_result, "while it should be", netloc_list[counter_netloc])
    #
    #     counter_netloc += 1
    #
    # print('\n')

    for url in input_list:
        parsed_result = URL(url.encode())
        path_result = parsed_result.path().decode()

        if path_result != path_list[counter_path]:
            if ((path_result == "" and path_list[counter_path] == '/') or (path_result == "/" and path_list[counter_path] == "")):
                pass
            else:
                print("unmatched path at", url, "the result is", path_result, "while it should be", path_list[counter_path])

        counter_path += 1


if __name__ == "__main__":
    main()
