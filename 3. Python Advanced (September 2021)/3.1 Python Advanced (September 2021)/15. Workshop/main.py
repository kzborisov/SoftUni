def create_board(rows_cnt, cols_cnt):
    return [[None] * cols_cnt for _ in range(rows_cnt)]


def print_board(field):
    def get_value(value):
        if value is not None:
            return value
        return 0

    for row in field:
        print([get_value(x) for x in row])


def is_player_choice_valid(board, player_choice):
    is_column_valid = 0 <= player_choice < len(board[0])
    is_column_full = is_column_valid and board[0][player_choice] is None
    return is_column_valid and is_column_full


def get_player_choice(player):
    choice = input(f"Player {player}, please choose a column\n")
    return int(choice) - 1


def apply_player_choice(board, player_choice, player):
    row_index = 0
    while row_index < len(board) and board[row_index][player_choice] is None:
        row_index += 1

    board[row_index - 1][player_choice] = player
    return row_index - 1, player_choice


def get_right_win_condition_values(board, row_index, col_index, max_col_index):
    right_win_condition = [board[row_index][c] for c in range(col_index, max_col_index)]
    return right_win_condition


def get_left_win_condition_values(board, row_index, col_index, min_col_index):
    left_win_condition = [board[row_index][c] for c in range(col_index, min_col_index, -1)]
    return left_win_condition


def get_up_win_condition_values(board, row_index, col_index, min_row_index):
    values = [board[r][col_index] for r in range(row_index, min_row_index, -1)]
    return values


def get_down_win_condition_values(board, row_index, col_index, max_row_index):
    values = [board[r][col_index] for r in range(row_index, max_row_index)]
    return values


def get_down_right_win_condition_values(board, row_index, col_index, max_row_index, max_col_index):
    values = []
    max_d = min(
        max_row_index - row_index,
        max_col_index - col_index
    )
    for d in range(max_d):
        r = row_index + d
        c = col_index + d
        values.append(board[r][c])
    return values


def get_down_left_win_condition_values(board, row_index, col_index, max_row_index, min_col_index):
    values = []
    max_d = min(
        max_row_index - row_index,
        abs(min_col_index - col_index)
    )
    for d in range(max_d):
        r = row_index + d
        c = col_index - d
        values.append(board[r][c])
    return values


def get_up_right_win_condition_values(board, row_index, col_index, min_row_index, max_col_index):
    # values = [board[r][col_index] for r in range(row_index, max_row_index)]
    # return values
    values = []
    max_d = min(
        abs(min_row_index - row_index),
        max_col_index - col_index
    )
    for d in range(max_d):
        r = row_index - d
        c = col_index + d
        values.append(board[r][c])
    return values


def get_up_left_win_condition_values(board, row_index, col_index, min_row_index, min_col_index):
    values = []
    max_d = min(
        abs(min_row_index - row_index),
        abs(min_col_index - col_index)
    )
    for d in range(max_d):
        r = row_index - d
        c = col_index - d
        values.append(board[r][c])
    return values


def check_win_condition(board, row_index, column_index, win_cnt):
    max_column_index = min(column_index + win_cnt, len(board[row_index]))
    min_column_index = max(column_index - win_cnt, -1)
    min_row_index = max(row_index - win_cnt, -1)
    max_row_index = min(row_index + win_cnt, len(board))

    right_win_condition = get_right_win_condition_values(
        board, row_index, column_index, max_column_index
    )
    left_win_condition = get_left_win_condition_values(
        board, row_index, column_index, min_column_index
    )
    up_win_condition = get_up_win_condition_values(
        board, row_index, column_index, min_row_index
    )
    down_win_condition = get_down_win_condition_values(
        board, row_index, column_index, max_row_index
    )
    up_left_condition = get_up_left_win_condition_values(
        board, row_index, column_index, min_row_index, min_column_index
    )
    up_right_condition = get_up_right_win_condition_values(
        board, row_index, column_index, min_row_index, max_column_index
    )
    down_left_condition = get_down_left_win_condition_values(
        board, row_index, column_index, max_row_index, min_column_index
    )
    down_right_condition = get_down_right_win_condition_values(
        board, row_index, column_index, max_row_index, max_column_index
    )

    possible_win_conditions = [
        right_win_condition,
        left_win_condition,
        up_win_condition,
        down_win_condition,
        up_right_condition,
        up_left_condition,
        down_right_condition,
        down_left_condition
    ]

    for values in possible_win_conditions:
        if len(values) == win_cnt and \
                len(set(values)) == 1:
            return True
    return False


def play(board):
    current_player, other_player = 1, 2
    while True:
        player_choice = get_player_choice(current_player)
        if not is_player_choice_valid(board, player_choice):
            print("Wrong column, try again!")
            continue

        row_index, column_index = apply_player_choice(
            board, player_choice, current_player
        )
        if check_win_condition(
                board, row_index, column_index, 4):
            print(f"The winner is player {current_player}")
            break

        # End of player's turn
        print_board(board)
        current_player, other_player = other_player, current_player


while True:
    board = create_board(6, 7)
    play(board)
