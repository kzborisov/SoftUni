import re

pattern = r"(^|(?<=\s))([A-Za-z0-9]+[A-za-z0-9\.\-\_]*\@[A-Za-z]+[A-Za-z\-]*(\.[a-zA-Z\.]+)+)\b"
text = input()

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())
