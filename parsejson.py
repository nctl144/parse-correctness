import json
import os


def remove_files(workpath, filename):
    if os.path.exists(os.path.join(workpath, filename)):
        os.remove(os.path.join(workpath, filename))

def write_result(path, input_list):
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

    '''
    delete generated files if presented
    '''
    c_workpath = os.path.join(os.getcwd(), "c")
    remove_files(c_workpath, "input-url.txt")
    remove_files(c_workpath, "scheme-url.txt")
    remove_files(c_workpath, "netloc-url.txt")

    rust_workpath = os.path.join(os.getcwd(), "urlparsetest")
    remove_files(rust_workpath, "input-url.txt")
    remove_files(rust_workpath, "scheme-url.txt")
    remove_files(rust_workpath, "netloc-url.txt")

    with open("urltest.json", 'r') as f:
        datastore = json.load(f)

    '''
    init the arrays for the txt files
    '''
    result_url_list = []
    scheme_list = []
    netloc_list = []

    for item in datastore:
        result_url, scheme = '', ''

        '''
        add the items from the json file to the arrays
        '''
        if 'href' in item:
            result_url = item['href']
            scheme = item['protocol']
            scheme = scheme[:-1] if scheme[-1] == ':' else scheme
            netloc = item['hostname']

        if result_url.strip() != '':
            result_url_list.append(result_url)
            scheme_list.append(scheme)
            netloc_list.append(netloc)


    '''
    Write the result to text files
    '''
    write_result("c/input-url.txt", result_url_list)
    write_result("c/scheme-url.txt", scheme_list)
    write_result("c/netloc-url.txt", netloc_list)

    write_result("urlparsetest/input-url.txt", result_url_list)
    write_result("urlparsetest/scheme-url.txt", scheme_list)
    write_result("urlparsetest/netloc-url.txt", netloc_list)


if __name__ == "__main__":
    main()
