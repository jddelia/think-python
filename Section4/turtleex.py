import math
import turtle

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 100)

def polygon(t, length, n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 5, 100)

def circle(t, r):
    circum = 2 * math.pi * r
    length = circum / n
    n = 50
    polygon(t, length, n)



turtle.mainloop()
