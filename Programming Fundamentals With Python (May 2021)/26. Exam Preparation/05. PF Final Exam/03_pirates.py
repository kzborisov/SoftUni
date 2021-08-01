def is_city_destroyed(cities_dict, town):
    if cities_dict[town]["population"] <= 0 or cities_dict[town]["gold"] <= 0:
        return True
    return False


def plunder(cities_dict, town, people, gold):
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    cities_dict[town]["population"] -= people
    cities_dict[town]["gold"] -= gold
    if is_city_destroyed(cities_dict, town):
        print(f"{town} has been wiped off the map!")
        cities_dict.pop(town)
    return cities_dict


def prosper(cities_dict, town, gold):
    if gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        cities_dict[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town]['gold']} gold.")
    return cities_dict


command = input()
cities = {}

while not command == "Sail":
    city, population, gold = command.split("||")
    if city not in cities:
        cities[city] = {"population": int(population), "gold": int(gold)}
    else:
        cities[city]['population'] += int(population)
        cities[city]['gold'] += int(gold)
    command = input()

command = input()
while not command == "End":
    cmd = command.split("=>")

    if cmd[0] == "Plunder":
        curr_town, people_count, curr_gold = cmd[1:]
        cities = plunder(cities, curr_town, int(people_count), int(curr_gold))
    elif cmd[0] == "Prosper":
        curr_town, curr_gold = cmd[1:]
        cities = prosper(cities, curr_town, int(curr_gold))
    command = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, info in sorted(cities.items(), key=lambda kvp: (-cities[kvp[0]]['gold'], kvp[0])):
        print(f"{city} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
