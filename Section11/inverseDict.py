''' This program writes an inverse of a dictionary
    key-value pair (to value-key) pair '''

d = dict()

''' The for loop below creates a dictionary to test function
    inverse_dict() '''

for i in range(11):
    if i % 2 == 0:
        d.setdefault(i, "even")
    else:
        d.setdefault(i, "odd")

def inverse_dict(dictionary):
    inverse = dict()
    for key in dictionary:
        val = dictionary[key]
        if val not in inverse:
            inverse.setdefault(val, [key])
        else:
            inverse[val].append(key)
    return inverse

print(inverse_dict(d))
