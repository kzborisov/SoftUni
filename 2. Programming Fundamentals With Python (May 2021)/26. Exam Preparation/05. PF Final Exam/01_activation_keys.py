def contains(string, substring):
    if substring in string:
        return f"{string} contains {substring}"
    return f"Substring not found!"


def flip(string, direction, start, end):
    if direction == "Upper":
        return string.replace(string[start:end], string[start:end].upper())
    elif direction == "Lower":
        return string.replace(string[start:end], string[start:end].lower())


def slice(string, start, end):
    return string.replace(string[start:end], "")


activation_key = input()
command = input()

while not command == "Generate":
    cmd = command.split(">>>")

    if cmd[0] == "Contains":
        print(contains(activation_key, cmd[1]))
    elif cmd[0] == "Flip":
        activation_key = flip(activation_key, cmd[1], int(cmd[2]), int(cmd[3]))
        print(activation_key)
    elif cmd[0] == "Slice":
        activation_key = slice(activation_key, int(cmd[1]), int(cmd[2]))
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")