from collections import deque


def add(side, values: deque, numbers=None):
    if side == "beginning":
        for number in reversed(numbers):
            values.appendleft(number)
    elif side == "end":
        for number in numbers:
            values.append(number)

    return list(values)


def remove(side, values: deque, number=None):
    if side == "beginning":
        if number:
            for _ in range(number):
                values.popleft()
        else:
            values.popleft()
    elif side == "end":
        if number:
            for _ in range(number):
                values.pop()
        else:
            values.pop()
    return list(values)


def list_manipulator(values, *args):
    if args[0] == "add":
        values = add(args[1], deque(values), args[2:])
    elif args[0] == "remove":
        try:
            values = remove(args[1], deque(values), int(args[2]))
        except IndexError:
            values = remove(args[1], deque(values))
    return values


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
