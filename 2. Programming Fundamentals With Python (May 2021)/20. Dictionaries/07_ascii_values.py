# Task 07. ASCII Values
characters = input().split(", ")
ascii_dict = {k: ord(k) for k in characters}
print(ascii_dict)
