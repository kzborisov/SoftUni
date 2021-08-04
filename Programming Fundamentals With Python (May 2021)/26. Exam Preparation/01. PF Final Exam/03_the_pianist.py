def add_piece(piece, composer, key):
    if piece not in pieces:
        pieces[piece] = {COMPOSER: composer, KEY: key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_piece(piece):
    if piece in pieces:
        pieces.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key):
    if piece in pieces:
        pieces[piece][KEY] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


n = int(input())
pieces = {}
COMPOSER = "composer"
KEY = "key"

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {COMPOSER: composer, KEY: key}

command = input()
while not command == "Stop":
    cmd = command.split("|")
    if cmd[0] == "Add":
        piece, composer, key = cmd[1:]
        add_piece(piece, composer, key)
    elif cmd[0] == "Remove":
        piece = cmd[1]
        remove_piece(piece)
    elif cmd[0] == "ChangeKey":
        piece, new_key = cmd[1:]
        change_key(piece, new_key)
    command = input()

for piece, piece_info in sorted(pieces.items(), key=lambda x: (x[0], x[1][COMPOSER])):
    print(f"{piece} -> Composer: {piece_info[COMPOSER]}, Key: {piece_info[KEY]}")

