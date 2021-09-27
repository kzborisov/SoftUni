size = int(input())

matrix = []
bunny_row, bunny_col = 0, 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_row, bunny_col = row, col

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
}

max_eggs = float("-inf")
best_path = []
best_direction = ""


def is_outside(r, c, size):
    return r < 0 or c < 0 or r >= size or c >= size


for direction, step in directions.items():
    eggs = 0
    path = []
    curr_row, curr_col = bunny_row, bunny_col

    while True:
        curr_row, curr_col = step(curr_row, curr_col)
        if is_outside(curr_row, curr_col, size):
            break
        if matrix[curr_row][curr_col] == "X":
            break

        eggs += int(matrix[curr_row][curr_col])
        path.append([curr_row, curr_col])

    if eggs > max_eggs:
        max_eggs, best_path, best_direction = eggs, path, direction

print(best_direction)
for step in best_path:
    print(step)
print(max_eggs)
