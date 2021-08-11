import re


def valid_ticket(ticket):
    return True if len(ticket) == 20 else False


def valid_combination(ticket):
    if valid_ticket(ticket):
        # TODO Fix The Regex (JUDGE: 70/100)
        pattern = r"([$]{6,10}|[@]{6,10}|[#]{6,10}|[\^]{6,10})"
        matches = [match.group() for match in re.finditer(pattern, ticket)]
        print(matches)
        if not matches:
            return f'ticket "{ticket}" - no match'
        else:
            if len(matches[0]) == 10 and len(matches[1]) == 10:
                return f'ticket "{ticket}" - {len(matches[0])}{matches[0][0]} Jackpot!'
            elif len(matches[0]) in range(6, 10) or len(matches[1]) in range(6, 10):
                return f'ticket "{ticket}" - {len(min(matches))}{matches[0][0]}'
    else:
        return "invalid ticket"


tickets = [x.strip() for x in input().split(", ")]

for ticket in tickets:
    print(valid_combination(ticket))
