# Task 04. Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        total_animals = len(self.mammals + self.fishes + self.birds)
        if species == "mammal":
            result = f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result = f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result = f"Birds in {self.zoo_name}: {', '.join(self.birds)}"
        return f"{result}"\
               f"\nTotal animals: {total_animals}"


zoo_name = input()
lines = int(input())
zoo = Zoo(zoo_name)

for _ in range(lines):
    zoo_info = input().split()
    zoo.add_animal(zoo_info[0], zoo_info[1])

animal_type = input()
print(zoo.get_info(animal_type))
