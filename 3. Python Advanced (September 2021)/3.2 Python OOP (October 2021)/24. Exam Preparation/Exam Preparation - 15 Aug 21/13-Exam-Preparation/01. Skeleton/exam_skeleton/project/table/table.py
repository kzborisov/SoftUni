from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: list[BakedFood] = []
        self.drink_orders: list[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved = False
        self.__initialize()

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + \
               sum(d.price for d in self.drink_orders)

    def clear(self):
        self.__initialize()

    def free_table_info(self):
        if not self.is_reserved:
            result = f"Table: {self.table_number}\n"
            result += f"Type: {self.__class__.__name__}\n"  # Not ok
            result += f"Capacity: {self.capacity}"
            return result

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def __initialize(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False
