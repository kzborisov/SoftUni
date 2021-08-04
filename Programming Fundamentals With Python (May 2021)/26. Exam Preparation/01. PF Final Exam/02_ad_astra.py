import re


def calculate_days(calories, cal_per_day):
    return calories // cal_per_day


text = input()
pattern = r"(?P<sep>(\|)|(#))"\
          r"(?P<item_name>[a-zA-Z\s]+)"\
          r"(?P=sep)"\
          r"(?P<expiration_date>\d{2}\/\d{2}\/\d{2})"\
          r"(?P=sep)"\
          r"(?P<calories>([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|10000))" \
          r"(?P=sep)"

matches = re.finditer(pattern, text)
total_calories = 0
items = []
CALORIES_PER_DAY = 2000
for match in matches:
    item = match.group('item_name')
    exp_date = match.group('expiration_date')
    calories = match.group('calories')
    items.append([item, exp_date, calories])
    total_calories += int(calories)

days = calculate_days(total_calories, CALORIES_PER_DAY)

print(f"You have food to last you for: {days} days!")
for item in items:
    food, exp_date, cals = item
    print(f"Item: {food}, Best before: {exp_date}, Nutrition: {cals}")
