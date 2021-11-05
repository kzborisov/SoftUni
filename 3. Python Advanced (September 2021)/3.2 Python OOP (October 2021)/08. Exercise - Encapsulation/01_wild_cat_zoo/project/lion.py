from project.animal import Animal


class Lion(Animal):
    money_for_care = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.money_for_care)
