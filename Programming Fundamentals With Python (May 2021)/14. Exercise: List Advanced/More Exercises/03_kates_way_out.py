import sys


def find_kate():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "k":
                return [row, col]


def display_maze(m, path):
    maze_copy = m[:]
    draw = ""

    for row in maze_copy:
        for col in row:
            draw += col
        draw += "\n"
    print(draw)


def move(path):
    row, col = path[-1]
    possible_moves = [
        [row, col + 1],  # Move Right
        [row, col - 1],  # Move Left
        [row - 1, col],  # Move Up
        [row + 1, col]   # Move Right
    ]

    for curr_move in possible_moves:
        print(path)
        if curr_move[0] == 0 or curr_move[0] == len(maze)-1 or curr_move[1] == 0 or curr_move[1] == len(maze[0])-1:
            return f"Kate got out in {len(path)} moves"
        if curr_move[0] not in range(len(maze)) or curr_move[1] not in range(len(maze[0])):
            continue

        maze[row][col] = "#"
        path.append(curr_move)
        print(path)
        move(path)

maze = [[x for x in input()] for _ in range(int(input()))]
pos = find_kate()
print(move([pos]))

