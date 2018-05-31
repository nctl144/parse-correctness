import json
import os


def remove_files(workpath, filename):
    if os.path.exists(os.path.join(workpath, filename)):
        os.remove(os.path.join(workpath, filename))

def write_rust(path, input_list):
    # remove the white line at the end for rust
    output_file = open(path, "w")
    i = 0
    while i < len(input_list):
        if i == len(input_list) - 1:
            output_file.write("{0}".format(input_list[i]))
        else:
            output_file.write("{0}\n".format(input_list[i]))
        i += 1
    output_file.close()


def main():

    # delete generated files if presented
    workpath = os.path.join(os.getcwd())
    remove_files(workpath, "input-url.txt")
    remove_files(workpath, "scheme-url.txt")

    rust_workpath = os.path.join(os.getcwd(), "urlparsetest")
    remove_files(rust_workpath, "input-url.txt")
    remove_files(rust_workpath, "scheme-url.txt")

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

    # remove the white line at the end for rust
    write_rust("urlparsetest/input-url.txt", result_url_list)
    write_rust("urlparsetest/scheme-url.txt", scheme_list)


if __name__ == "__main__":
    main()
