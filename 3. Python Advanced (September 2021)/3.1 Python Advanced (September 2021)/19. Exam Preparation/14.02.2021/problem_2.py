def is_index_valid(r, c, matrix_size):
    return r in range(size) and c in range(size)


def is_wall_hit(r, c, matrix, walls_coordinates):
    return matrix[r][c] in walls_coordinates


size = int(input())
field = []

player_row, player_col = 0, 0
walls = []
for row in range(size):
    field.append(input().split())
    for col in range(size):
        if field[row][col] == "P":
            player_row, player_col = row, col
        elif field[row][col] == "X":
            walls.append([row, col])

directions = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
}

collected_coins = 0
game_won = False
path = []

while True:
    command = input()

    if command not in directions:
        continue

    next_row, next_col = directions[command](player_row, player_col)
    if not is_index_valid(next_row, next_col, field) or field[next_row][next_col] == "X":
        collected_coins //= 2
        break
    path.append([next_row, next_col])
    collected_coins += int(field[next_row][next_col])
    if collected_coins >= 100:
        game_won = True
        break
    player_row, player_col = next_row, next_col

if game_won:
    print(f"You won! You've collected {collected_coins} coins.")
else:
    print(f"Game over! You've collected {collected_coins} coins.")

print("Your path: ")
print(*path, sep="\n")
