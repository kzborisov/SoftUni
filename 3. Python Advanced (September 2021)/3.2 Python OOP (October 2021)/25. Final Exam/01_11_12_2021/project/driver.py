class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None  # One driver drives only one car
        self.number_of_wins = 0  # Increase when the driver wins

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name should contain at least one character!")
        self.__name = value
