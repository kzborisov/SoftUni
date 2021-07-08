def is_broken(lst, idx):
    if lst[idx] <= 0:
        return True
    return False


def fire(idx, damage):
    if idx in range(len(warship_status)):
        warship_status[idx] -= damage
        if is_broken(warship_status, idx):
            print("You won! The enemy ship has sunken.")
            exit()


def defend(start, end, damage):
    if 0 <= start < len(pirate_ship_status) and 0 <= end < len(pirate_ship_status):
        for i in range(start, end+1):
            pirate_ship_status[i] -= damage
            if is_broken(pirate_ship_status, i):
                print("You lost! The pirate ship has sunken.")
                exit()


def repair(idx, hp):
    if idx in range(len(pirate_ship_status)):
        pirate_ship_status[idx] += hp
        if pirate_ship_status[idx] > max_health:
            pirate_ship_status[idx] = max_health


def get_status():
    threshold = max_health * 0.2
    count = 0
    for section in pirate_ship_status:
        if section < threshold:
            count += 1
    print(f"{count} sections need repair.")


pirate_ship_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
max_health = int(input())
command = input()

while not command == "Retire":
    cmd = command.split()[0]
    if cmd == "Fire":
        idx = int(command.split()[1])
        dmg = int(command.split()[2])
        fire(idx, dmg)
    elif cmd == "Defend":
        start_idx = int(command.split()[1])
        end_idx = int(command.split()[2])
        dmg = int(command.split()[3])
        defend(start_idx, end_idx, dmg)
    elif cmd == "Repair":
        idx = int(command.split()[1])
        health = int(command.split()[2])
        repair(idx, health)
    elif cmd == "Status":
        get_status()

    command = input()

print(f"Pirate ship status: {sum(pirate_ship_status)}")
print(f"Warship status: {sum(warship_status)}")
