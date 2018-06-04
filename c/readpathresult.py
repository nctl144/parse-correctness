arr = []

with open("path-result.txt", "r") as f:
    for path in f:
        if path[-1] == '\n':
            path = path.replace('\n', '')

        if path != "":
            path = '/' + path

        arr.append(path)


result = []

with open('path-url.txt', 'r') as f:
    for path in f:
        if path[-1] == '\n':
            path = path.replace('\n', '')

        result.append(path)

input = []

with open('input-url.txt', 'r') as f:
    for url in f:
        if url[-1] == '\n':
            url = url.replace('\n', '')

        input.append(url)


counter = 0
for path in arr:
    if path != result[counter]:
        if (path == "" and result[counter] == "/") or path[1:] == result[counter]:
            pass
        else:
            print("unmatched path at", input[counter], "the result is", path, "expected", result[counter])


    counter += 1
