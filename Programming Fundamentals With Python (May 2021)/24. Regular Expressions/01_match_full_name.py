import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()

names = re.findall(pattern, text)
print(*names, sep=" ")
