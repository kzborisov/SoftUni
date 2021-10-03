def is_index_valid(r, c, matrix_size):
    return r in range(matrix_size) and c in range(matrix_size)


size = int(input())

matrix = []
snake_row, snake_col = 0, 0
burrows = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "S":
            snake_row, snake_col = row, col
        elif matrix[row][col] == "B":
            burrows.append((row, col))

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

food_eaten = 0
# matrix[snake_row][snake_col] = "."

while food_eaten < 10:
    command = input()
    if command not in directions:
        continue

    next_row, next_col = directions[command](snake_row, snake_col)
    if not is_index_valid(next_row, next_col, size):
        break

    current_cell = matrix[next_row][next_col]
    matrix[snake_row][snake_col] = "."
    matrix[next_row][next_col] = "S"

    if current_cell == "*":
        food_eaten += 1
    elif (next_row, next_col) in burrows:
        burrows.remove((next_row, next_col))
        snake_row, snake_col = burrows[0]
        matrix[next_row][next_col] = "."
        continue

    snake_row, snake_col = next_row, next_col

if food_eaten < 10:
    matrix[snake_row][snake_col] = "."
    print("Game over!\n"
          f"Food eaten: {food_eaten}")
else:
    matrix[snake_row][snake_col] = "S"
    print("You won! You fed the snake.\n"
          f"Food eaten: {food_eaten}")
[print(*x, sep="") for x in matrix]
