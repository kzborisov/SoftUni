from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    _possible_fish_type = ("SaltwaterFish",)

    def __init__(self, name):
        super().__init__(name, 25)
