import re

places = input()
pattern = r"((=){1}|(\/){1})(?P<place>[A-Z][A-Za-z]{2,})(\1)"

matches = re.finditer(pattern, places)
travel_points = 0
destinations = []
for match in matches:
    place = match.group('place')
    destinations.append(place)
    travel_points += len(place)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
