rows, cols = map(int, input().split())
word = input()

matrix = []
word_index = 0

for row in range(rows):
    matrix.append([None] * cols)
    for col in range(cols):
        col_idx = col if row % 2 == 0 else cols - 1 - col
        matrix[row][col_idx] = word[word_index]
        word_index = (word_index + 1) % len(word)

for row in matrix:
    print(*row, sep="")
