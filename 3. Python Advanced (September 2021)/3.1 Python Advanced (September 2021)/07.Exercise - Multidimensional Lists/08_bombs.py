def is_inside(r, c, matrix_size):
    if 0 <= r < matrix_size and 0 <= c < matrix_size:
        return True
    return False


def get_surrounding_bombs(r, c, matrix_size):
    bombs = []
    # Up
    if is_inside(r - 1, c, matrix_size):
        bombs.append([r - 1, c])
    # up - left
    if is_inside(r - 1, c - 1, matrix_size):
        bombs.append([r - 1, c - 1])
    # Left
    if is_inside(r, c - 1, matrix_size):
        bombs.append([r, c - 1])
    # Down left
    if is_inside(r + 1, c - 1, matrix_size):
        bombs.append([r + 1, c - 1])
    # Down
    if is_inside(r + 1, c, matrix_size):
        bombs.append([r + 1, c])
    # Down Right
    if is_inside(r + 1, c + 1, matrix_size):
        bombs.append([r + 1, c + 1])
    # Right
    if is_inside(r, c + 1, matrix_size):
        bombs.append([r, c + 1])
    # Up right
    if is_inside(r - 1, c + 1, matrix_size):
        bombs.append([r - 1, c + 1])
    return bombs


def is_bomb_alive(r, c):
    return matrix[r][c] > 0


size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
bomb_coordinates = [[int(x) for x in x.split(",")] for x in input().split()]

for bomb in bomb_coordinates:
    row, col = bomb
    surrounding_bombs = get_surrounding_bombs(row, col, size)

    current_bomb = matrix[row][col]
    if is_bomb_alive(row, col):
        matrix[row][col] = 0
        for surrounding_bomb in surrounding_bombs:
            r, c = surrounding_bomb
            if is_bomb_alive(r, c):
                matrix[r][c] -= current_bomb

alive_cells = [x for row in matrix for x in row if x > 0]
sum_alive_cells = sum(alive_cells)
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum_alive_cells}")
[print(*x) for x in matrix]
