# Task 03. Characters in Range

def chars_in_range(start, end):
    return " ".join([chr(x) for x in range(ord(start)+1, ord(end))])


first_char = input()
second_char = input()
print(chars_in_range(first_char, second_char))
