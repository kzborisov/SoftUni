from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _possible_fish_type = ("FreshwaterFish",)

    def __init__(self, name):
        super().__init__(name, 50)
