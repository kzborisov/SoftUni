rows, cols = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]


def is_valid_position(r, c, rows, cols):
    return r in range(rows) and c in range(cols)


while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    cmd = command[0]

    if cmd[0] == "swap" or not len(command) == 5:
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if not is_valid_position(row1, col1, rows, cols) or \
            not is_valid_position(row2, col2, rows, cols):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for r in matrix:
        print(" ".join([str(x) for x in r]))
