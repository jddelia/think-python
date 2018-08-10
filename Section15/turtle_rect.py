# This program creates a turtle with an OOP rectangle.

import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle:

    def __init__(self, corner, height, width):
        self.corner = corner
        self.height = height
        self.width = width

corner_1 = Point(10, 10)
rect_1 = Rectangle(corner_1, 25, 50)

turt = turtle.Turtle()

def turtle_rect(t, rect):

    for i in range(2):
        t.fd(rect.width)
        t.lt(90)
        t.fd(rect.height)
        t.lt(90)

turtle_rect(turt, rect_1)

turtle.mainloop()
