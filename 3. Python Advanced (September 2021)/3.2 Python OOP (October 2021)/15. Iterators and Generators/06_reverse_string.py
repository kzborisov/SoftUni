def reverse_text(string):
    idx = len(string) - 1

    while idx >= 0:
        yield string[idx]
        idx -= 1


a = reverse_text("step")
for char in a:
    print(char, end='')
