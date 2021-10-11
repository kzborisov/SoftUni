from time import time


def binary_search(values, target, start_index, end_index):
    if start_index >= end_index:
        raise ValueError(f"{target} not in list!")
    mid = (start_index + end_index) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return binary_search(values, target, mid + 1, end_index)
    elif values[mid] > target:
        return binary_search(values, target, start_index, mid)


def slow_binary_search(values, target):
    if not values:
        raise ValueError(f"{target} not in list!")
    mid = len(values) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return mid + 1 + slow_binary_search(values[mid + 1:], target)
    elif values[mid] > target:
        return slow_binary_search(values[:mid], target)


def measure(action, repeat_count=1):
    start_time = time()
    for i in range(repeat_count):
        action()
    end_time = time()
    print(f"-- executed in {end_time - start_time} seconds!")


def find_all(values):
    s = 0
    for val in values:
        s += binary_search(values, val, 0, len(values))
    return s


def find2_all(values):
    s = 0
    for val in values:
        s += slow_binary_search(values, val)
    return s


values = [x for x in range(2 ** 15)]

measure(lambda: find_all(values))
measure(lambda: find2_all(values))
