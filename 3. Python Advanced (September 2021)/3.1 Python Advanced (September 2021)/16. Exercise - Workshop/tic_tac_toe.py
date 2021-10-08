from errors import InvalidPositionError


def read_first_player_sign(first_player_name):
    """Get the sign of the first player, while X or O"""
    while True:
        first_player_sign = input(
            f"{first_player_name} would you like to play with X or O? "
        ).upper()
        if first_player_sign in ["X", "O"]:
            return first_player_sign


def read_players_info():
    """Get players info - [player 1 name, player 1 sign]"""
    first_player_name = input("Player one name: ")
    second_player_name = input("Player two name: ")
    first_player_sign = read_first_player_sign(first_player_name)
    second_player_sign = "O" if first_player_sign == "X" else "X"

    return ([first_player_name, first_player_sign],
            [second_player_name, second_player_sign])


def print_board_numeration():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def get_coords_by_pos(position):
    if position == 1:
        return 0, 0
    if position == 2:
        return 0, 1
    if position == 3:
        return 0, 2
    if position == 4:
        return 1, 0
    if position == 5:
        return 1, 1
    if position == 6:
        return 1, 2
    if position == 7:
        return 2, 0
    if position == 8:
        return 2, 1
    if position == 9:
        return 2, 2
    raise InvalidPositionError(
        f"{position} is invalid. "
        "Please provide a valid position in range [1-9]!"
    )


def draw_board(matrix):
    for row in matrix:
        print("| ", end="")
        print(" | ".join(str(x) for x in row), end="")
        print(" |")


def is_board_full(matrix):
    for row in matrix:
        is_row_full = all([x != " " for x in row])
        if not is_row_full:
            return False
    return True


def is_winner(matrix, sign):
    # horizontal
    for idx in matrix:
        if all([x == sign for x in idx]):
            return True
    # vertical
    size = len(matrix)
    for col in range(size):
        won = True
        for row in range(size):
            if not matrix[row][col] == sign:
                won = False
                break
        if won:
            return True

    # primary diagonal
    won = True
    for idx in range(size):
        if not matrix[idx][idx] == sign:
            won = False
            break
    if won:
        return True

    # secondary diagonal
    won = True
    for idx in range(size):
        if not matrix[idx][size - 1 - idx] == sign:
            won = False
            break
    return won


def play(matrix, player1, player2):
    turns = 0
    player_turns = {0: player1, 1: player2}
    while True:
        name, sign = player_turns[turns % 2]

        try:
            position = int(input(f"{name} choose a free position [1-9]: "))
            row, col = get_coords_by_pos(position)
            if not matrix[row][col] == " ":
                raise InvalidPositionError(f"{position} is already taken! "
                                           "Please choose a free position!")

            matrix[row][col] = sign
            turns += 1
            draw_board(matrix)

            if is_winner(matrix, sign):
                print(f"{name} has won!")
                break

            if is_board_full(matrix):
                print("Draw!")
                break
        except ValueError:
            print("Please provide a valid position!")
        except InvalidPositionError as err:
            print(err)


player_one, player_two = read_players_info()
print_board_numeration()
print(f"{player_one[0]} starts first!")

board = [[" "] * 3 for _ in range(3)]
play(board, player_one, player_two)
