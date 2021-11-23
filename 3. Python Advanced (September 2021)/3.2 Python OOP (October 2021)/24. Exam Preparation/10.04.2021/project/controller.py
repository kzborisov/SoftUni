from project.aquarium.freshwater_aquarium import FreshwaterAquarium  # noqa
from project.aquarium.saltwater_aquarium import SaltwaterAquarium  # noqa
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament  # noqa
from project.decoration.plant import Plant  # noqa
from project.fish.freshwater_fish import FreshwaterFish  # noqa
from project.fish.saltwater_fish import SaltwaterFish  # noqa


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        try:
            aquarium = globals()[aquarium_type]
            aquarium = aquarium(aquarium_name)
        except KeyError:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        try:
            decoration = globals()[decoration_type]
            decoration = decoration()
        except KeyError:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__find_aquarium(aquarium_name)
        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        try:
            fish = globals()[fish_type]
            fish = fish(fish_name, fish_species, price)
        except KeyError:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium(aquarium_name)
        result = aquarium.add_fish(fish)
        return result

    def feed_fish(self, aquarium_name):
        aquarium = self.__find_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.__find_aquarium(aquarium_name)
        value = aquarium.total_fish_price + aquarium.total_decoration_price
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        return "\n".join(str(a) for a in self.aquariums)

    def __find_aquarium(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
