from collections import deque

SIZE = 7
BULLSEYE = (3, 3)


class PLayer:
    def __init__(self, name):
        self.name = name
        self.score = 501
        self.throws = 0


def read_board(size):
    matrix = []
    for r in range(size):
        matrix.append(input().split())
    return matrix


def is_index_valid(r, c, matrix_size):
    return r in range(matrix_size) and c in range(matrix_size)


def get_corresponding_numbers_sum(r, c, matrix):
    left = int(matrix[r][0])
    right = int(matrix[r][-1])
    up = int(matrix[0][c])
    down = int(matrix[-1][c])
    return sum([left, right, up, down])


player_one_name, player_two_name = input().split(", ")
board = read_board(SIZE)
players_turn = deque([PLayer(player_one_name), PLayer(player_two_name)])

while True:
    row, col = map(int, input().strip("()").split(", "))
    player = players_turn.popleft()
    players_turn.append(player)
    player.throws += 1

    if (row, col) == BULLSEYE:
        break

    if not is_index_valid(row, col, SIZE):
        continue

    current_cell = board[row][col]
    if current_cell.isdigit():
        player.score -= int(current_cell)
    elif current_cell == "D":
        sum_numbers = get_corresponding_numbers_sum(row, col, board)
        player.score -= (2 * sum_numbers)
    elif current_cell == "T":
        sum_numbers = get_corresponding_numbers_sum(row, col, board)
        player.score -= (3 * sum_numbers)

    if player.score <= 0:
        break

print(f"{player.name} won the game with {player.throws} throws!")
