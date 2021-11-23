from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut

    def recharge_astronauts_oxygen(self, value):
        for astronaut in self.astronauts:
            astronaut.increase_oxygen(value)

    def get_suitable_astronauts(self):
        return [ast for ast in sorted(self.astronauts, key=lambda a: -a.oxygen) if ast.oxygen > 30]

    def __str__(self):
        return '\n'.join([str(astronaut) for astronaut in self.astronauts])
