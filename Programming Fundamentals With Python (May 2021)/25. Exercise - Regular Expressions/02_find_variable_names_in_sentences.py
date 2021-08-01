import re

pattern = r"\b_(?P<variable>[A-Za-z0-9]+)\b"
text = input()

variables = re.finditer(pattern, text)
variables = [var.group('variable') for var in variables]
print(*variables, sep=",")
