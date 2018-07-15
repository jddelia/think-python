#This program is a square root calculator.
#It uses the Newton method.

import math
import decimal

def newtsquare():
    a = int(input("Select a number to figure out its square root: "))
    x = 10
    while abs(x - math.sqrt(a)) > 0.00001:
        x = (x + a/x) / 2
    print(round(x, 4))

newtsquare()
