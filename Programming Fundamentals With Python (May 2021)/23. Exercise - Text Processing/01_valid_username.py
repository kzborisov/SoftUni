def is_length_valid(user):
    return True if len(user) in range(3, 17) else False


def all_chars_valid_chars(user):
    """contains only letters, numbers, hyphens, and underscores"""
    # if not user.isalnum() or not contains_only_underscores(user):
    #     return False
    # return True
    for ch in user:
        if not ch.isalnum() and not ch in ["-", "_"]:
            return False
    return True


def no_redundant_symbols(user):
    pass


usernames = input().split(", ")
for username in usernames:
    if is_length_valid(username) and all_chars_valid_chars(username):
        print(f"{username}")

