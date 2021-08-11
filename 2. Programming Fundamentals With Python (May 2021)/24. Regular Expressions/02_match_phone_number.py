import re

pattern = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}\b"
text = input()

valid_phones = re.finditer(pattern, text)
valid_phones = [phone.group() for phone in valid_phones]
print(*valid_phones, sep=", ")
