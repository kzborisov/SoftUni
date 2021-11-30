from project import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        # TODO: Remove validation if it fails
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    def find_astronauts_for_mission(self, count: int, min_oxygen: int):
        return sorted(
            [x for x in self.astronauts if x.oxygen > min_oxygen],
            key=lambda x: -x.oxygen
        )[:count]
