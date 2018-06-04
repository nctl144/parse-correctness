# result from uriparser
arr = []

with open('hosttext.txt', 'r') as f:
    for item in f:
        string_list = item.split("seperated by")

        string_list = [element.strip() for element in string_list]

        for netloc in string_list:
            if netloc[-1] == '\n':
                netloc.replace('\n', '')

        # print(string_list[0], string_list[1])

        result = string_list[1][:-(len(string_list[0]))]
        if result == "" or result == "X" or result == "(null)" or result == '/':
            arr.append('')
        else:
            arr.append(result)


output_file = open("netloc-result.txt", "w")
i = 0
while i < len(arr):
    if i == len(arr) - 1:
        output_file.write("{0}".format(arr[i]))
    else:
        output_file.write("{0}\n".format(arr[i]))
    i += 1
output_file.close()
