elements = input().split()
pair = input()
moves = 0

while not pair == "end":
    first_idx = int(pair.split()[0])
    second_idx = int(pair.split()[1])
    moves += 1
    if first_idx == second_idx or \
            first_idx not in range(len(elements)) or \
            second_idx not in range(len(elements)):
        middle_idx = len(elements) // 2
        elements.insert(middle_idx, f"-{moves}a")
        elements.insert(middle_idx, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_idx] == elements[second_idx]:
        print(f"Congrats! You have found matching elements - {elements[first_idx]}!")
        elements = [x for idx, x in enumerate(elements) if
                    idx not in [first_idx, second_idx]]
    elif not elements[first_idx] == elements[second_idx]:
        print(f"Try again!")

    if not elements:
        print(f"You have won in {moves} turns!")
        break

    pair = input()

if pair == "end":
    print(f"Sorry you lose :(\n"
          f"{' '.join(elements)}")
