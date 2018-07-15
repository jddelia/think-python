#Circle Perimeter

import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def area(a):
    area = (math.pi * 2) * a
    return area

def circle_area(xc, yc, xp, yp):
    radius = radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result
