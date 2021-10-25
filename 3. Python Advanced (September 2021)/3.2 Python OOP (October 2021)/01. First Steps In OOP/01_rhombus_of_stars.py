n = int(input())


def print_line(spaces, stars):
    line = "".join([' '] * spaces)
    line_stars = " ".join(["*"] * stars)
    print(line + line_stars)


for i in range(n):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces, stars)

for i in range(n - 2, -1, -1):
    spaces = n - i - 1
    stars = i + 1
    print_line(spaces, stars)
