from collections import deque


def fill_the_box(*args):
    box_size = args[0] * args[1] * args[2]
    args = deque(args[3:])
    while args:
        curr_arg = args.popleft()
        if curr_arg == "Finish":
            break

        box_size -= curr_arg
        if box_size < 0:
            args.remove("Finish")
            return f"No more free space! You have {sum(args) + abs(box_size)} more cubes."

    return f"There is free space in the box. You could put {abs(box_size // 1)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
