from project.animal import Animal


class Reptile(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

