from collections import deque


def calculate_pureness(arguments):
    pureness = 0
    for index, element in enumerate(arguments):
        pureness += element * index
    return pureness


def best_list_pureness(arguments, k):
    arguments = deque(arguments)
    pureness_value = calculate_pureness(arguments)
    count_rotations = 0
    for i in range(k + 1):
        current_pureness = calculate_pureness(arguments)
        if current_pureness > pureness_value:
            pureness_value = current_pureness
            count_rotations = i
        arguments.appendleft(arguments.pop())
    return f"Best pureness {pureness_value} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)