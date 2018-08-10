# This program creates a circle with OOP.

from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Rectangle:

    def __init__(self, corner, height, width):
        self.corner = corner
        self.height = height
        self.width = width

center_1 = Point(150, 100)
circle_1 = Circle(center_1, 75)

corner_1 = Point(100, 100)
rect_1 = Rectangle(corner_1, 25, 50)

def rect_in_circle(rect, circle):
    distance = sqrt(abs(corner_1.x - circle.center.x)**2 + abs(corner_1.y - circle.center.y)**2)
