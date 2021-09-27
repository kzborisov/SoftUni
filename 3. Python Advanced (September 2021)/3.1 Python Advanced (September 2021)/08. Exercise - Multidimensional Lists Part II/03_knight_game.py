def is_valid_index(r, c, board_size):
    return r in range(board_size) and c in range(board_size)


def calculate_kills(matrix, r, c):
    kills = 0
    possible_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)
    ]
    for idx in range(len(possible_moves)):
        row = r + possible_moves[idx][0]
        col = c + possible_moves[idx][1]
        if is_valid_index(row, col, len(matrix)) and \
                matrix[row][col] == "K":
            kills += 1
    return kills


size = int(input())
board = [[x for x in list(input())] for _ in range(size)]

removed_knights = 0
while True:
    max_kills = 0
    knight_position = set()

    for r in range(size):
        for c in range(size):
            if board[r][c] == "K":
                kills = calculate_kills(board, r, c)
                if kills > max_kills:
                    max_kills = kills
                    knight_position = (r, c)

    if not knight_position:
        break

    row, col = knight_position
    board[row][col] = "O"
    removed_knights += 1

print(removed_knights)
