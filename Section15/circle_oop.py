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

center_1 = Point(150, 100)

circle_1 = Circle(center_1, 75)

center_2 = Point(75, 50)

print(circle_1.__dict__)

def point_in_circle(point, circle):

    distance = sqrt(abs(point.x - circle.center.x)**2 + abs(point.y - circle.center.y)**2)

    print(distance)
    if distance <= circle.radius:
        return True
    else:
        return False

print(point_in_circle(center_2, circle_1))
