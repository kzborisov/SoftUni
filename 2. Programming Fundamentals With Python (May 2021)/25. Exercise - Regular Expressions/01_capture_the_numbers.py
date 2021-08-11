import re

pattern = r"\d+"
text = []
line = input()
while line:
    text.append(line)
    line = input()

text = "".join(text)
numbers = re.findall(pattern, text)
print(*numbers)
