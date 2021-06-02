# Task 10. Bread Factory
energy = 100
coins = 100
MAX_ENERGY = 100
ORDER_ENERGY = 30
REST_ENERGY = 50
events = input()

separated_events = [x.split('-') for x in events.split('|')]
events_managed = True

for event in separated_events:
    event_type = event[0]
    event_number = int(event[1])

    if event_type == 'rest':
        gained_energy = min(event_number, MAX_ENERGY - energy)
        energy += gained_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif event_type == 'order':
        if energy - ORDER_ENERGY >= 0:
            coins += event_number
            energy -= ORDER_ENERGY
            print(f'You earned {event_number} coins.')
        else:
            energy += REST_ENERGY
            print('You had to rest!')

    else:
        if not coins - event_number <= 0:
            coins -= event_number
            print(f'You bought {event_type}.')
        else:
            events_managed = False
            print(f'Closed! Cannot afford {event_type}.')
            break

if events_managed:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
