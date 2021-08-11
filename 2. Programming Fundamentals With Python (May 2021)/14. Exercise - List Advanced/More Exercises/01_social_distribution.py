# Task 01. More Exercises Social Distribution

population = list(map(int, input().split(", ")))
min_wealth = int(input())

for idx in range(len(population)):
    max_id = population.index(max(population))

    while population[idx] < min_wealth:
        population[idx] += 1
        population[max_id] -= 1

if all(x >= min_wealth for x in population):
    print(population)
else:
    print("No equal distribution possible")
