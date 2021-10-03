from collections import deque


def is_index_valid(r, c, matrix_size):
    return r in range(matrix_size) and c in range(matrix_size)


size = 8
board = []
king_coords = ()
queens = deque()


# directions = {
#     "up": lambda r, c: (r - 1, c),
#     "down": lambda r, c: (r + 1, c),
#     "left": lambda r, c: (r, c - 1),
#     "right": lambda r, c: (r, c + 1),
#     "primary_up": lambda r, c: (r - 1, c - 1),
#     "primary_down": lambda r, c: (r - 1, c - 1),
#     "secondary_up": lambda r, c: (r - 1, c + 1),
#     "secondary_down": lambda r, c: (r + 1, c - 1),
# }

def check_up(r, c, board_size):
    while True:
        r -= 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


def check_down(r, c, board_size):
    while True:
        r += 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


def check_left(r, c, board_size):
    while True:
        c -= 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


def check_right(r, c, board_size):
    while True:
        c += 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


def check_primary_up(r, c, board_size):
    while True:
        r -= 1
        c -= 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


def check_primary_down(r, c, board_size):
    while True:
        r += 1
        c += 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


def check_secondary_up(r, c, board_size):
    while True:
        r -= 1
        c += 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


def check_secondary_down(r, c, board_size):
    while True:
        r += 1
        c -= 1
        if not is_index_valid(r, c, board_size):
            break
        cell_value = board[r][c]
        if cell_value == "Q":
            return False
        elif cell_value == "K":
            return True


for row in range(size):
    board.append(input().split())
    for col in range(size):
        if board[row][col] == "K":
            king_coords = row, col
        elif board[row][col] == "Q":
            queens.append((row, col))

successfull = False
for queen in queens:
    row, col = queen

    if check_up(row, col, size) or \
            check_down(row, col, size) or \
            check_left(row, col, size) or \
            check_right(row, col, size) or \
            check_primary_up(row, col, size) or \
            check_primary_down(row, col, size) or \
            check_secondary_up(row, col, size) or \
            check_secondary_down(row, col, size):
        print([row, col])
        successfull = True

if not successfull:
    print("The king is safe!")
