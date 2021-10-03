def is_index_valid(r, c, matrix_size):
    return r in range(matrix_size) and c in range(matrix_size)


string = input()
size = int(input())

field = []
player_row, player_col = 0, 0
for row in range(size):
    field.append(list(input()))
    for col in range(size):
        if field[row][col] == "P":
            player_row, player_col = row, col

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

moves_cnt = int(input())
for move in range(moves_cnt):
    command = input()
    if command not in directions:
        continue

    next_row, next_col = directions[command](player_row, player_col)

    if not is_index_valid(next_row, next_col, size):
        if string:
            string = string[:-1]
        continue

    if field[next_row][next_col].isalpha():
        string += field[next_row][next_col]

    field[player_row][player_col] = "-"
    field[next_row][next_col] = "P"
    player_row, player_col = next_row, next_col

print(string)
[print(*row ,sep="") for row in field]