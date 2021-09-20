from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = 0


def calculate_honey(matched_bee, curr_symbol, matched_nectar):
    if curr_symbol == "+":
        return abs(matched_bee + matched_nectar)
    elif curr_symbol == "-":
        return abs(matched_bee - matched_nectar)
    elif curr_symbol == "*":
        return abs(matched_bee * matched_nectar)
    elif curr_symbol == "/":
        if matched_nectar == 0:
            return 0
        return abs(matched_bee / matched_nectar)


while True:
    if not working_bees or not nectar:
        break

    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if first_bee <= last_nectar:
        symbol = symbols.popleft()
        current_honey = calculate_honey(first_bee, symbol, last_nectar)
        honey += current_honey
    else:
        working_bees.appendleft(first_bee)

print(f"Total honey made: {honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
