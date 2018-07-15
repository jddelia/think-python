#Factorial Calculator

import math

def factorial(n):
    global sum
    sum += (n * (n-1))
    print(n)
    print()
    print(sum)
    if n == 0:
            return
    else:
            n -= 1
            factorial(n)
