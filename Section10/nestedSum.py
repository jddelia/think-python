# This program find the total sum of
# a list, including nested lists.

t = [[1,2], [3], [4,5,6]]

def nested_sum(n):
    count = 0
    for i in n:
        count += sum(i)
    print(count)
nested_sum(t)
