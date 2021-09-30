def flights(*args):
    passengers_count = {}
    for index in range(0, len(args) - 1, 2):
        flight = args[index]
        passengers = args[index + 1]
        if 'Finish' in [flight, passengers]:
            return passengers_count
        if flight not in passengers_count:
            passengers_count[flight] = int(passengers)
            continue
        passengers_count[flight] += int(passengers)
    return passengers_count


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
