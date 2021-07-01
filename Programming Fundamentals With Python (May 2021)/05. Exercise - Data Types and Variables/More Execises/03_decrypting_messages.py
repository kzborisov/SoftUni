# Task 03. More Exercises Decrypting Messages
key = int(input())
lines = int(input())

msg = ''

for line in range(1, lines+1):
    letter = input()
    msg += chr(ord(letter) + key)

print(msg)
