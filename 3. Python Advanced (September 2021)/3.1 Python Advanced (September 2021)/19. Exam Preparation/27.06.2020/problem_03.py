from collections import deque


def list_manipulator(numbers, *args):
    args = deque(args)
    command = args.popleft()
    front_or_back = args.popleft()
    numbers = deque(numbers)

    if command == "add" and front_or_back == "beginning":
        while args:
            numbers.appendleft(args.pop())
    elif command == "add" and front_or_back == "end":
        while args:
            numbers.append(args.popleft())
    elif command == "remove" and front_or_back == "beginning":
        if args:
            for i in range(args[0]):
                numbers.popleft()
        else:
            numbers.popleft()
    elif command == "remove" and front_or_back == "end":
        if args:
            for i in range(args[0]):
                numbers.pop()
        else:
            numbers.pop()
    return list(numbers)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
