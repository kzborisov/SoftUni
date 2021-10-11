def print_triangle(size):
    for row in range(1, size + 2):
        [print(x, end=" ") for x in range(1, row)]
        print()
    for row in range(size, 0, -1):
        [print(x, end=" ") for x in range(1, row)]
        print()
