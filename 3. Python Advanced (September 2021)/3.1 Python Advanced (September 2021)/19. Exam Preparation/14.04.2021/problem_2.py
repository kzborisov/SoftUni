from collections import deque


def is_valid_index(r, c, matrix_size):
    return 0 <= r < matrix_size and 0 <= c < matrix_size


def corresponding_sum(r, c, matrix):
    left = int(matrix[r][0])
    right = int(matrix[r][-1])
    up = int(matrix[0][c])
    down = int(matrix[-1][c])
    return sum([left, right, up, down])


size = 7
players = deque(input().split(", "))
scores = {
    players[0]: [501, 0],
    players[1]: [501, 0],
}

board = []
for row in range(size):
    board.append(input().split())
winner = None

while not winner:
    # Get the current player
    current_player = players.popleft()
    players.append(current_player)

    # Increment each player's throws count
    scores[current_player][1] += 1

    # Read input
    line = input()
    if line == "":
        break

    # Get coordinates
    x, y = [int(x) for x in line.strip("()").split(", ")]

    # Check for invalid coordinates
    if not is_valid_index(x, y, size):
        continue
    current_cell = board[x][y]
    if current_cell.isdigit():
        scores[current_player][0] -= int(current_cell)
    elif current_cell == "D":
        points = corresponding_sum(x, y, board) * 2
        scores[current_player][0] -= points
    elif current_cell == "T":
        points = corresponding_sum(x, y, board) * 3
        scores[current_player][0] -= points
    elif current_cell == "B":
        winner = current_player

    # Check for winner
    if scores[current_player][0] <= 0:
        winner = current_player

throws = scores[winner][1]
print(f"{winner} won the game with {throws} throws!")
