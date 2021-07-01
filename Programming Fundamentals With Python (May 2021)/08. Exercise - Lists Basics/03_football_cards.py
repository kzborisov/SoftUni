# Task 03. Football Cards
cards = input().split()
a_team = [x for x in range(1, 12)]
b_team = [x for x in range(1, 12)]
is_terminated = False


def remove_player(player, team):
    try:
        team.remove(player)
    except ValueError:
        pass


for card in cards:
    card = card.split('-')
    if card[0] == 'A':
        remove_player(int(card[1]), a_team)
    elif card[0] == 'B':
        remove_player(int(card[1]), b_team)

    if len(a_team) < 7 or len(b_team) < 7:
        is_terminated = True
        break

print(f'Team A - {len(a_team)}; Team B - {len(b_team)}')
if is_terminated:
    print('Game was terminated')
