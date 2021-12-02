from abc import ABC, abstractmethod


class BakedFood(ABC):
    __INVALID_NAME_EXCEPTION = "Name cannot be empty string or white space!"
    __INVALID_PRICE_EXCEPTION = "Price cannot be less than or equal to zero!"

    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError(self.__INVALID_NAME_EXCEPTION)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError(self.__INVALID_PRICE_EXCEPTION)
        self.__price = value
