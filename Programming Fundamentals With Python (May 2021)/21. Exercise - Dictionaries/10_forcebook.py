def user_exists(force_side_dict, user):
    for users in force_side_dict.values():
        if user in users:
            return True
    return False


def remove_user(force_side_dict, user):
    for side, users in force_side_dict.items():
        if user in users:
            force_side_dict[side].remove(user)


def add_to_force_side(force_side_dict, user, side):
    if not user_exists(force_side_dict, user) and side not in force_side_dict:
        force_side_dict[side] = [user]
    elif not user_exists(force_side_dict, user):
        force_side_dict[side].append(user)


def change_force_side(force_side_dict, user, side):
    if side not in force_side_dict and not user_exists(force_side_dict, user):
        force_side_dict[side] = [user]
    elif not user_exists(force_side_dict, user):
        if side not in force_side_dict:
            force_side_dict[side] = []
        force_side_dict[side].append(user)
    elif user_exists(force_side_dict, user):
        remove_user(force_side_dict, user)
        if side not in force_side_dict:
            force_side_dict[side] = []
        force_side_dict[side].append(user)
    print(f"{user} joins the {side} side!")


command = input()
force_side_users = {}

while not command == "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        add_to_force_side(force_side_users, force_user, force_side)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        change_force_side(force_side_users, force_user, force_side)
    command = input()


for side, users in sorted(force_side_users.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if not len(users) == 0:
        print(f"Side: {side}, Members: {len(users)}")
    for user in sorted(users):
        print(f'! {user}')


# Task 1 regex -> \b[A-Z][a-z]+ [A-Z][a-z]+\b