username = input()

while True:
    command = input()
    if command == "Registration":
        break

    command_args = command.split()
    command_name = command_args[0]

    if command_name == "Letters":
        state = command_args[1]
        if state == "Lower":
            username = username.lower()
        elif state == "Upper":
            username = username.upper()
        print(username)
    elif command_name == "Reverse":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if start_index in range(len(username)) and end_index in range(len(username)):
            substring_to_reverse = username[start_index:end_index+1][::-1]
            print(substring_to_reverse)
    elif command_name == "Substring":
        substring = command_args[1]
        if substring not in username:
            print(f"The username {username} doesn't contain {substring}.")
            continue
        username = username.replace(substring, "", 1)
        print(username)
    elif command_name == "Replace":
        char = command_args[1]
        username = username.replace(char, "-")
        print(username)
    elif command_name == "IsValid":
        char = command_args[1]
        if char not in username:
            print(f"{char} must be contained in your username.")
            continue
        print("Valid username.")

