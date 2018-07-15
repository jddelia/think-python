# Program testing the uses of dictionaries.

import pprint

def histogram(n):
    d = dict()
    for i in n:
        d[i] = d.get(i, 0)
        d[i] += 1
    print(d)

histogram("brontasaurus")
