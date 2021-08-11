def move(msg, letters_ctn):
    return ''.join([msg[letters_ctn:], msg[:letters_ctn]])


def insert_value(msg, idx, value):
    return msg[:idx] + value + msg[idx:]


def change_all(msg, substring, replacement):
    return msg.replace(substring, replacement)


encrypted_msg = input()
command = input()
while not command == "Decode":
    cmd = command.split("|")
    if cmd[0] == "Move":
        curr_letter_ctn = int(cmd[1])
        encrypted_msg = move(encrypted_msg, curr_letter_ctn)
    elif cmd[0] == "Insert":
        curr_idx, curr_value = cmd[1:]
        encrypted_msg = insert_value(encrypted_msg, int(curr_idx), curr_value)
    elif cmd[0] == "ChangeAll":
        curr_substring, curr_replacement = cmd[1:]
        encrypted_msg = change_all(encrypted_msg, curr_substring, curr_replacement)
    command = input()

print(f"The decrypted message is: {encrypted_msg}")
