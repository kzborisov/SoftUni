import re


def replace_chars(string, ch):
    pattern = ch + "{2,}"
    return re.sub(pattern, ch, string)


text = input()

for ch in text:
    text = replace_chars(text, ch)

print(text)
