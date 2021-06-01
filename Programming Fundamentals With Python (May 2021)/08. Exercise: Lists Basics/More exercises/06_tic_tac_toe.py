# Task 06. More Exercises Tic Tac Toe
def winner(board):
    # Horizontal
    for row in range(BOARD_SIZE):
        if len(set(board[row])) == 1:
            return board[row][0]
    # Vertical
    for column in range(BOARD_SIZE):
        if len(set([row[column] for row in board])) == 1:
            return board[0][column]
    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]


line_1 = input().split()
line_2 = input().split()
line_3 = input().split()


game_board = [line_1, line_2, line_3]
BOARD_SIZE = len(game_board)
win = winner(game_board)

if win == '1':
    print('First player won')
elif win == '2':
    print('Second player won')
else:
    print('Draw!')
