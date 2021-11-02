from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
