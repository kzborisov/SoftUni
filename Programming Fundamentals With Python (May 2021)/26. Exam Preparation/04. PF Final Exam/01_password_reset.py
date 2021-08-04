def take_odd(passphrase):
    passphrase ="".join(
        [passphrase[x] for x in range(1, len(passphrase)) if not x % 2 == 0])
    print(passphrase)
    return passphrase


def cut_pass(passphrase, idx, length):
    word_to_remove = ""
    while len(word_to_remove) < length:
        word_to_remove += passphrase[idx]
        idx += 1
    passphrase = passphrase.replace(word_to_remove, "", 1)
    print(passphrase)
    return passphrase


def substitute(passphrase, old_substring, new_substring):
    if old_substring in passphrase:
        while old_substring in passphrase:
            passphrase = passphrase.replace(old_substring, new_substring)
            print(passphrase)
        return passphrase
    else:
        print(f"Nothing to replace!")
        return passphrase


password = input()
command = input()

while not command == "Done":
    cmd = command.split()

    if cmd[0] == "TakeOdd":
        password = take_odd(password)
    elif cmd[0] == "Cut":
        curr_idx, curr_length = cmd[1:]
        password = cut_pass(password, int(curr_idx), int(curr_length))
    elif cmd[0] == "Substitute":
        old_string, new_string = cmd[1:]
        password = substitute(password, old_string, new_string)

    command = input()

print(f"Your password is: {password}")
