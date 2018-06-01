arr = []

with open('hosttext.txt', 'r') as f:
    for item in f:
        if item[-1:] == '\n':
            item = item.replace('\n', '')

        if item == "(null)" or item == "X":
            item = ""

        arr.append(item)

counter = 0

with open('netloc-url.txt', 'r') as f:
    for netloc in f:
        if arr[counter] == "" and (netloc.strip() != "" or netloc.strip() != "\n"):
            print("unmatched netloc at", netloc)

        if arr[counter] != "" and (netloc.strip() == "" or netloc.strip() == "\n"):
            print("unmatched netloc at", netloc)

        counter += 1

print(counter)
