from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. " \
               f"{self.name} is a {self.age} year old " \
               f"{self.gender} {self.__class__.__name__}"
