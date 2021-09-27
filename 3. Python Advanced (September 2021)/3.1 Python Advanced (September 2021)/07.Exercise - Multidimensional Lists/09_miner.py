def is_inside(r, c, matrix_size):
    return r in range(matrix_size) and c in range(matrix_size)


size = int(input())
commands = input().split()

matrix = []
miner_row, miner_col = 0, 0
end_row, end_col = 0, 0
initial_coal = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "s":
            miner_row, miner_col = row, col
        elif matrix[row][col] == "e":
            end_row, end_col = row, col
        elif matrix[row][col] == "c":
            initial_coal += 1

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

collected_coal = initial_coal

for move in commands:
    next_row, next_col = directions[move](miner_row, miner_col)
    if not is_inside(next_row, next_col, size):
        continue

    cell_value = matrix[next_row][next_col]
    if cell_value == "c":
        collected_coal -= 1
        matrix[next_row][next_col] = "*"
    elif cell_value == "e":
        print(f'Game over! ({next_row}, {next_col})')
        exit()

    miner_row, miner_col = next_row, next_col


if collected_coal <= 0:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
else:
    print(f"{collected_coal} pieces of coal left. ({miner_row}, {miner_col})")
