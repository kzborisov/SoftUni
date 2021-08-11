import re

pattern = r'^>>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<qty>\d+)$'

furniture = []
total_price = 0

command = input()
while not command == "Purchase":
    match = re.match(pattern, command)
    if match:
        furniture_name = match.group('furniture')
        price = float(match.group('price'))
        qty = int(match.group('qty'))

        furniture.append(furniture_name)
        total_price += price * qty
    command = input()

print("Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_price}")
