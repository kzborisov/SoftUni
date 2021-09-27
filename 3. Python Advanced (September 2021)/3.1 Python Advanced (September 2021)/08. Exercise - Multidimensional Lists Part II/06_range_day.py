size = 5

matrix = []
player_row, player_col = 0, 0
targets_count = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        element = matrix[row][col]
        if element == "A":
            player_row, player_col = row, col
        elif element == "x":
            targets_count += 1

n = int(input())


def next_position(direction, r, c, steps=1):
    if direction == "right":
        return r, c + steps
    if direction == "left":
        return r, c - steps
    if direction == "up":
        return r - steps, c
    if direction == "down":
        return r + steps, c


def is_outside(size, r, c):
    return r < 0 or c < 0 or r >= size or c >= size


hit_targets = []
for _ in range(n):
    line_args = input().split()
    command = line_args[0]
    direction = line_args[1]

    if command == "move":
        steps = int(line_args[2])
        next_player_row, next_player_col = next_position(direction, player_row, player_col, steps)

        if is_outside(size, next_player_row, next_player_col):
            continue
        if matrix[next_player_row][next_player_col] != ".":
            continue

        matrix[next_player_row][next_player_col] = "A"
        matrix[player_row][player_col] = "."
        player_row, player_col = next_player_row, next_player_col

    elif command == "shoot":
        bullet_row, bullet_col = next_position(direction, player_row, player_col)

        while True:
            if is_outside(size, bullet_row, bullet_col):
                break
            if matrix[bullet_row][bullet_col] == "x":
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = "."
                break

            bullet_row, bullet_col = next_position(direction, bullet_row, bullet_col)

        if len(hit_targets) == targets_count:
            break

if len(hit_targets) == targets_count:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_count - len(hit_targets)} targets left.")

for target in hit_targets:
    print(target)
