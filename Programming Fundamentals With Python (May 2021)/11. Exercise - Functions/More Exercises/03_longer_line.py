# Task 03. More Exercises - Longer Line
import math

def distance_to_center(x, y):
    """math.sqrt((x2-x1)^2 + (y2 - y1)^2)
    Given that (x1, y1) = (0, 0) -> center"""
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    return distance


def line_length(x, y, x1, y1):
    """math.sqrt((x2-x1)^2 + (y2 - y1)^2)
    Given that (x1, y1) = (0, 0) -> center"""
    distance = math.sqrt(math.pow((x1 - x), 2) + math.pow(y1 - y, 2))
    return distance


def create_line(x, y, x1, y1):
    first = distance_to_center(x, y)
    second = distance_to_center(x1, y1)
    if first <= second:
        return f"({math.floor(x)}, {math.floor(y)})({math.floor(x1)}, {math.floor(y1)})"
    return f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x)}, {math.floor(y)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

line_one = line_length(x1, y1, x2, y2)
line_two = line_length(x3, y3, x4, y4)


if line_one <= line_two:
    line = create_line(x3, y3, x4, y4)
else:
    line = create_line(x1, y1, x2, y2)
print(line)
