# Task 03. More Exercises Messaging
numbers = input().split()
string_with_chars = input()
text = [x for x in string_with_chars]
msg = ''
for num in numbers:
    num_to_int = [int(x) for x in num]
    ind = sum(num_to_int)
    while ind > len(string_with_chars):
        ind -= len(string_with_chars)
    msg += text[ind]
    text.pop(ind)

print(msg)
