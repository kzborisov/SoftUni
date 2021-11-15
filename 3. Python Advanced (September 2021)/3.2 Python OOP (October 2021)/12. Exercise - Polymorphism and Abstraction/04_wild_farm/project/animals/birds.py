from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    __weight_increase = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.eat(food, self.__weight_increase)


class Hen(Bird):
    __weight_increase = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        self.eat(food, self.__weight_increase)