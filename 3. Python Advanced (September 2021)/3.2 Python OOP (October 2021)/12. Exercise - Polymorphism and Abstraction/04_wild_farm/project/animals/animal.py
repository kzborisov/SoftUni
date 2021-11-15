from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def eat(self, food, gained_weight):
        self.food_eaten += food.quantity
        self.weight += gained_weight * food.quantity


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} [{self.name}, " \
               f"{self.wing_size}, " \
               f"{self.weight}, " \
               f"{self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} [{self.name}, " \
               f"{self.weight}, " \
               f"{self.living_region}, " \
               f"{self.food_eaten}]"
