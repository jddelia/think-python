#Conditionals Ex. 2

import math

print("This program verifies Fermat's Last Theorem.\n\n Select four variables.")
print()
a = int(input("Select the first variable a: "))
b = int(input("Select the second variable b: "))
c = int(input("Select the third variable c: "))
n = int(input("Select the fourth variable n: "))

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, fermat was wrong!")
    else:
        print("\n No, that doesn't work.")

check_fermat(1, 2, 3, 2)
