from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)