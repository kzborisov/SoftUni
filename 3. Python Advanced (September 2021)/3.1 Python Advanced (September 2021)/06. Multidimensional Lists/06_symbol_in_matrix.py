import sys

size = int(input())
matrix = [list(input()) for _ in range(size)]
searched_symbol = input()

for row in range(size):
    for col in range(size):
        if matrix[row][col] == searched_symbol:
            print((row, col))
            sys.exit()

print(f"{searched_symbol} does not occur in the matrix")
