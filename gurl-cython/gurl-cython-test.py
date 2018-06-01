from pygurl import URL
from timeit import default_timer as timer

import json

total = 0

with open('../.txt') as f:
    f = [url.encode() for url in f]

    for url in f:

        start = timer()

        a = URL(url)

        end = timer()

        total += end - start

print("the total time is", total, "seconds")
