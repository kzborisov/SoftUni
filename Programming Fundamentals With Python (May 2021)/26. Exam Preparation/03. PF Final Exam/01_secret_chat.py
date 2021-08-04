def insert_space(msg, idx):
    msg = msg[:idx] + " " + msg[idx:]
    print(msg)
    return msg


def reverse(msg, substring):
    if substring in msg:
        msg = msg.replace(substring, "", 1)
        msg += substring[::-1]
        print(msg)
        return msg
    else:
        print("error")
        return msg


def change_all(msg, old_substring, new_substring):
    msg = msg.replace(old_substring, new_substring)
    print(msg)
    return msg


concealed_msg = input()
command = input()

while not command == "Reveal":
    cmd = command.split(":|:")
    operation = cmd[0]
    if operation == "InsertSpace":
        curr_idx = int(cmd[1])
        concealed_msg = insert_space(concealed_msg, curr_idx)
    elif operation == "Reverse":
        curr_substring = cmd[1]
        concealed_msg = reverse(concealed_msg, curr_substring)
    elif operation == "ChangeAll":
        curr_substring, replacement = cmd[1:]
        concealed_msg = change_all(concealed_msg, curr_substring, replacement)
    command = input()

print(f"You have a new text message: {concealed_msg}")
