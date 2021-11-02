from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
