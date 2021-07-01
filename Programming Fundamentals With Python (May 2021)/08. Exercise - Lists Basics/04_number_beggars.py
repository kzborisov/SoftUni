# Task 04. Number Beggars
numbers = input().split(', ')
count_of_beggars = int(input())

beggars = [[] for _ in range(1, count_of_beggars+1)]

while len(numbers) > 0:
    for ind in range(len(beggars)):
        try:
            beggars[ind].append(int(numbers[0]))
            numbers.pop(0)
        except IndexError:
            pass

print([sum(x) for x in beggars])
