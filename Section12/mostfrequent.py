''' This program creates a function that takes
    a string as an argument and returns the frequency of
    letters used. '''

d = dict()
rev_dict = dict()

def most_frequent(string):
    lst = []
    for i in string:
        if i == " ":
            continue
        if i not in d:
            d[i] = 1 # Adding items to dictionary.
        else:
            d[i] += 1

    for k, v in d.items():
        if v not in rev_dict:
            rev_dict[v] = ""
        if k not in rev_dict.values():
            rev_dict[v] += k + " "
    print(rev_dict)

    ''' Values are taken from a dictionary and placed in
        a list. '''

    for k in rev_dict.keys():
        lst.append(str(k))
    lst.sort(reverse=True)

    print(lst)

    for i in lst:
        if i in rev_dict.keys():
            lst[lst.index(i)] += rev_dict[i]
    return lst

print(most_frequent("test one two three"))
