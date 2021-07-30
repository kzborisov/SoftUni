substring = input()
text = input()

while substring in text:
    text = text.replace(substring, "")

print(text)
