# result from uriparser
arr = []

with open('netloc-result.txt', 'r') as f:
    for item in f:
        if item[-1:] == '\n':
            item = item.replace('\n', '')

        if item == "(null)" or item == "X":
            item = ""

        arr.append(item)

# for i in arr:
#     print("this is the item", i, "asdqwe")

counter = 0

# expected result
netloc_url = []

with open('netloc-url.txt', 'r') as f:
    for netloc in f:
        if netloc.strip() == "\n":
            netloc_url.append("")
        else:
            netloc_url.append(netloc.strip())

input_url = []
with open('input-url.txt') as f:
    for url in f:
        if url[-1:] == '\n':
            url = url.replace('\n', '')

        input_url.append(url)

print("this is the length of each array", len(arr), len(netloc_url), len(input_url))

for netloc in netloc_url:
    if netloc != arr[counter]:
        print("unmatched netloc at", input_url[counter], "the result should be", netloc, "while it is", arr[counter])

    counter += 1
