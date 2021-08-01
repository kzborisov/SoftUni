import re

pattern = r"(?P<day>\d{2})([./-])(?P<month>[A-Z][a-z]{2})(\2)(?P<year>\d{4})"
text = input()

valid_dates = re.finditer(pattern, text)

for date in valid_dates:
    valid_date = date.groupdict()
    print(f"Day: {valid_date['day']}, Month: {valid_date['month']}, Year: {valid_date['year']}")
