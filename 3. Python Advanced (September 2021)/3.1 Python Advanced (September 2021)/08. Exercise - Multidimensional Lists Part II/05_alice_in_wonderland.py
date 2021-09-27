size = int(input())

matrix = []
alice_row, alice_col = 0, 0
targets_count = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        element = matrix[row][col]
        if element == "A":
            alice_row, alice_col = row, col


def next_position(direction, r, c):
    if direction == "right":
        return r, c + 1
    if direction == "left":
        return r, c - 1
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c


def is_outside(size, r, c):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


teabags = 0
matrix[alice_row][alice_col] = "*"

while True:
    direction = input()
    alice_row, alice_col = next_position(direction, alice_row, alice_col)
    if is_outside(size, alice_row, alice_col):
        break

    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = "*"
    if cell_value == "R":
        break

    if cell_value.isdigit():
        teabags += int(cell_value)
        if teabags >= 10:
            break

if teabags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=" ")
