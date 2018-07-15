#This program checks whether a list is sorted
# and returns True or False.

t = [1, 2, 3]

def is_sorted(n):
    nsort = n[:]
    nsort.sort()
    if n == nsort:
        print("True")
    else:
        print("False")

is_sorted(t)
