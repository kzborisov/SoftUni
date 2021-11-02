from project.animal import Animal


class Mammal(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

