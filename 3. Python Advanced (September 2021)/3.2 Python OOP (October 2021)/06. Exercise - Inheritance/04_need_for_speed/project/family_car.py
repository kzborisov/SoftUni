from project.car import Car


class FamilyCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
