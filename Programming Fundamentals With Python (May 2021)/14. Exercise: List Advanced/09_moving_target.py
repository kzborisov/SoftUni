# Task 09. Moving Target
def shoot(idx, power, lst):
    if idx in range(len(lst)):
        lst[idx] -= power
        if lst[idx] <= 0:
            lst.pop(idx)


def add_target(idx, value, lst):
    if idx in range(len(lst)):
        lst.insert(idx, value)
    else:
        print("Invalid placement!")


def strike_target(idx, radius, lst):
    global targets
    if idx not in range(len(lst)) or \
            idx-radius not in range(idx) or \
            idx+radius not in range(idx, len(lst)):
        print("Strike missed!")
    else:
        targets = [(y, x)[1] for y, x in enumerate(lst) if y not in range(idx-radius, idx+radius+1)]


targets = list(map(int, input().split()))
cmd = input()

while not cmd == "End":
    command = cmd.split()[0]
    cmd_args = list(map(int, cmd.split()[1:]))

    if command == "Shoot":
        shoot(cmd_args[0], cmd_args[1], targets)
    elif command == "Add":
        add_target(cmd_args[0], cmd_args[1], targets)
    elif command == "Strike":
        strike_target(cmd_args[0], cmd_args[1], targets)

    cmd = input()

print("|".join(list(map(str, targets))))
