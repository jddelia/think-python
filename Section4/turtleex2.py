import math
import turtle

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, an):
    for i in range(8):
        arc(t, r, an)
        t.lt(135)
        arc(t, r, an)
        t.lt(135)
        arc(t, r - 100, an)

petal(bob, 100, 45)

def petal1(t, r, an):
    for i in range(7):
        arc(t, r, an)
        t.lt(128.7)
        arc(t, r, an)
        t.lt(128.7)
        arc(t, r - 87.7, an)

petal1(bob, 87.7, 51.3)

def petal3(t, r, an):
    for i in range(20):
        arc(t, r, an)
        t.lt(162)
        arc(t, r, an)
        t.lt(162)
        arc(t, r - 250, an)

petal3(bob, 250, 18)

turtle.mainloop()
