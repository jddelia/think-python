# This program memoizes the Acermann function.

d = dict()

def ackermann(m, n):
    if m == 0:
        n + 1
    elif m > 0 and n == 0:
        ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        ackermann(m - 1, ackermann(m, n - 1))
