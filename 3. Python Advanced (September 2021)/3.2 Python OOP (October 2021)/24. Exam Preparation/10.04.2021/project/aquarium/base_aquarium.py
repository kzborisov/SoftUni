from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    _possible_fish_type = ("FreshwaterFish", "SaltwaterFish")

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        if fish.get_type() not in self._possible_fish_type:
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.get_type()} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    @property
    def total_fish_price(self):
        return sum(f.price for f in self.fish)

    @property
    def total_decoration_price(self):
        return sum(d.price for d in self.decorations)

    def __str__(self):
        return f"{self.name}:\n" \
               f"Fish: {' '.join(f.name for f in self.fish) or 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
