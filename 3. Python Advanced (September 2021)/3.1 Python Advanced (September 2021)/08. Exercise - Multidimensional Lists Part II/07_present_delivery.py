def is_outside(r, c, size):
    return r < 0 or c < 0 or r >= size or c >= size


def get_houses_in_range(size, r, c):
    houses = []
    if not is_outside(r - 1, c, size):
        houses.append([r - 1, c])
    if not is_outside(r + 1, c, size):
        houses.append([r + 1, c])
    if not is_outside(r, c - 1, size):
        houses.append([r, c - 1])
    if not is_outside(r, c + 1, size):
        houses.append([r, c + 1])
    return houses


presents_cnt = int(input())
n = int(input())

matrix = []
santa_row, santa_col = 0, 0
initial_nice_kids_cnt = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa_row, santa_col = row, col
        elif matrix[row][col] == "V":
            initial_nice_kids_cnt += 1

moves = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}

nice_kids_cnt = initial_nice_kids_cnt

while True:
    move = input()
    if move == "Christmas morning":
        break

    next_santa_row, next_santa_col = moves[move](santa_row, santa_col)

    cell_value = matrix[next_santa_row][next_santa_col]

    if cell_value == "C":
        houses_in_range = get_houses_in_range(n, next_santa_row, next_santa_col)
        for row, col in houses_in_range:
            if matrix[row][col] == "X":
                presents_cnt -= 1
            if matrix[row][col] == "V":
                presents_cnt -= 1
                nice_kids_cnt -= 1

            matrix[row][col] = "-"
            if presents_cnt == 0:
                break
    elif cell_value == "V":
        nice_kids_cnt -= 1
        presents_cnt -= 1

    matrix[next_santa_row][next_santa_col] = "S"
    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = next_santa_row, next_santa_col

    if presents_cnt <= 0:
        break

if presents_cnt <= 0 < nice_kids_cnt:
    print("Santa ran out of presents!")

[print(*x) for x in matrix]

if nice_kids_cnt == 0:
    print(f"Good job, Santa! {initial_nice_kids_cnt} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_cnt} nice kid/s.")
