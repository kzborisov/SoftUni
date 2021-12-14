from abc import ABC, abstractmethod


class Car(ABC):
    MIN_SPEED_LIMIT = None
    MAX_SPEED_LIMIT = None

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False  # One car can be driven only by one driver

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.validate_speed_limit(value)
        self.__speed_limit = value

    @abstractmethod
    def validate_speed_limit(self, value):
        pass
