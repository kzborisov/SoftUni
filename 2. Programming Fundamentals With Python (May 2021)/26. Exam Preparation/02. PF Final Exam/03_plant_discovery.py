def average(lst):
    if lst:
        return sum(lst) / len(lst)
    return 0.0


def valid_plant(plant):
    return True if plant in plants else False


def rate(plant, rating):
    if valid_plant(plant):
        plants[plant][RATING].append(rating)
    else:
        print("error")


def update(plant, new_rarity):
    if valid_plant(plant):
        plants[plant][RARITY] = new_rarity
    else:
        print("error")


def reset(plant):
    if valid_plant(plant):
        plants[plant][RATING].clear()
    else:
        print("error")


n = int(input())
plants = {}
RARITY = "rarity"
RATING = "rating"

for _ in range(n):
    curr_plant, rarity = input().split("<->")
    plants[curr_plant] = {RARITY: int(rarity), RATING: []}

command = input()
while not command == "Exhibition":
    cmd = command.split(": ")
    if cmd[0] == "Rate":
        curr_plant, curr_rating = cmd[1].split(" - ")
        rate(curr_plant, int(curr_rating))
    elif cmd[0] == "Update":
        curr_plant, curr_new_rarity = cmd[1].split(" - ")
        update(curr_plant, int(curr_new_rarity))
    elif cmd[0] == "Reset":
        curr_plant = cmd[1]
        reset(curr_plant)

    command = input()


print("Plants for the exhibition:")
for plant, plant_info in sorted(plants.items(), key=lambda x: (-x[1][RARITY], -average(x[1][RATING]))):
    print(f"- {plant}; Rarity: {plant_info[RARITY]}; Rating: {average(plant_info[RATING]):.2f}")
