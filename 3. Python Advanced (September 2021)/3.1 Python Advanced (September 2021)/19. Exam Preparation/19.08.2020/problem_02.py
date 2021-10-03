def is_index_valid(r, c, matrix_size):
    return r in range(matrix_size) and c in range(matrix_size)


def get_near_bombs(field, r, c):
    directions = {
        'up': lambda x, y: (x - 1, y),
        'down': lambda x, y: (x + 1, y),
        'left': lambda x, y: (x, y - 1),
        'right': lambda x, y: (x, y + 1),
        'up_left': lambda x, y: (x - 1, y - 1),
        'up_right': lambda x, y: (x - 1, y + 1),
        'down_right': lambda x, y: (x + 1, y + 1),
        'down_left': lambda x, y: (x + 1, y - 1),
    }
    bombs_count = 0
    for direction in directions:
        next_row, next_col = directions[direction](r, c)
        if not is_index_valid(next_row, next_col, len(field)):
            continue

        if field[next_row][next_col] == "*":
            bombs_count += 1
    return bombs_count


size = int(input())
bombs_cnt = int(input())

positions = []
for _ in range(bombs_cnt):
    coordinates = input()
    row, col = coordinates.strip("()").split(", ")
    positions.append((int(row), int(col)))

matrix = [[None for _ in range(size)] for _ in range(size)]

for row in range(size):
    for col in range(size):
        if (row, col) in positions:
            matrix[row][col] = "*"

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "*":
            continue
        bombs = get_near_bombs(matrix, row, col)
        matrix[row][col] = bombs
[print(*x) for x in matrix]
