# Task 02. More Exercises - Center Point
import math


def distance_to_center(x, y):
    """math.sqrt((x2-x1)^2 + (y2 - y1)^2)
    Given that (x1, y1) = (0, 0) -> center"""
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return distance


def center_point(x1, y1, x2, y2):
    distance_x = distance_to_center(x1, y1)
    distance_y = distance_to_center(x2, y2)
    if distance_x <= distance_y:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_point(x1, y1, x2, y2))
