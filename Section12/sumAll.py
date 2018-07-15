''' This program takes any number of arguments,
    and returns their sum. '''

a, b, c = 1, 2, 3

def sumall(*args):
    print(sum(args))

sumall(a, b, c)
