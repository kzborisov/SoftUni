guests = {}
unliked_meals = 0

while True:
    command = input()
    if command == "Stop":
        break

    command_args = command.split("-")
    command_name = command_args[0]
    guest = command_args[1]
    meal = command_args[2]

    if command_name == "Like":
        if guest not in guests:
            guests[guest] = []

        if meal in guests[guest]:
            continue
        guests[guest].append(meal)

    elif command_name == "Unlike":
        if guest not in guests:
            print(f"{guest} is not at the party.")
            continue

        if meal not in guests[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            continue

        print(f"{guest} doesn't like the {meal}.")
        unliked_meals += 1
        guests[guest].remove(meal)


for guest, guest_info in sorted(guests.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{guest}: {', '.join(guest_info)}")

print(f"Unliked meals: {unliked_meals}")
