SIZE = 6


def read_matrix(matrix_size):
    matrix = []
    for _ in range(matrix_size):
        matrix.append(input().split())
    return matrix


def get_buckets_positions(matrix_size, matrix):
    buckets_positions = []
    for r in range(matrix_size):
        for c in range(matrix_size):
            if matrix[r][c] == "B":
                buckets_positions.append((int(r), int(c)))
    return buckets_positions


def is_index_valid(r, c, matrix_size, matrix):
    return r in range(matrix_size) and \
           c in range(matrix_size) and \
           matrix[r][c].isalpha()


def calculate_point(matrix, r, c):
    points = 0
    for i in range(len(matrix)):
        cell = matrix[i][c]
        if cell.isdigit():
            points += int(cell)
    return points


board = read_matrix(SIZE)
buckets = get_buckets_positions(SIZE, board)
score = 0

for _ in range(3):
    row, col = map(int, input().strip("()").split(", "))
    if not is_index_valid(row, col, SIZE, board):
        continue

    if (row, col) in buckets:
        buckets.remove((row, col))
        score += calculate_point(board, row, col)

if score >= 300:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
elif 200 <= score < 300:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
elif 100 <= score < 200:
    print(f"Good job! You scored {score} points, and you've won Football.")
else:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
