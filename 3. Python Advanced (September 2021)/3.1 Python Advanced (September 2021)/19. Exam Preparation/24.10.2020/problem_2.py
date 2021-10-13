import sys
from io import StringIO

test_input = """. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . ."""

test_input_2 = """. . . . . . . .
. . . Q . . . .
. . . . . . . .
. . . . . . . .
Q . . . Q . . .
. . K . . . . .
. . . . . . Q .
. . . Q . . . ."""

sys.stdin = StringIO(test_input)
# sys.stdin = StringIO(test_input_2)

KING_SYMBOL = "K"
QUEEN_SYMBOL = "Q"


def read_board(n):
    matrix = []
    for row in range(n):
        matrix.append(input().split())
    return matrix


def find_king_positions(matrix):
    for row in range(len(matrix)):
        # for col in range(len(matrix[0])):
        #     if matrix[row][col] == KING_SYMBOL:
        #         return row, col
        if KING_SYMBOL in board[row]:
            col = board[row].index(KING_SYMBOL)
            return row, col


def search_with_deltas(matrix, king_pos, deltas):
    rows_cnt = len(board)
    col_cnt = len(board[0])
    row_index, col_index = king_pos
    delta_row, delta_col = deltas

    while True:
        if not is_index_valid(row_index, rows_cnt) or \
                not is_index_valid(col_index, col_cnt):
            return None
        if matrix[row_index][col_index] == QUEEN_SYMBOL:
            return row_index, col_index

        row_index += delta_row
        col_index += delta_col


def get_capturing_queens(matrix, king_pos):
    deltas = [
        # Row, Col
        (0, -1),  # left
        (-1, -1),  # Left Up
        (-1, 0),  # Up
        (-1, +1),  # Up Right
        (0, +1),  # Right
        (+1, +1),  # Down Right
        (+1, 0),  # Down
        (+1, -1),  # Down Left
    ]
    queens = [
        search_with_deltas(matrix, king_pos, delta)
        for delta in deltas
    ]
    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        [print(queen) for queen in queens]
    else:
        print(f"King is safe!")


def is_index_valid(value, matrix_size):
    return value in range(matrix_size)


board = read_board(8)
king = find_king_positions(board)
queens = get_capturing_queens(board, king)
print_result(queens)
