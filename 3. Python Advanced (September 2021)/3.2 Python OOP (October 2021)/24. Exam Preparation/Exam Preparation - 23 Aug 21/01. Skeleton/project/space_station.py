from project import AstronautRepository
from project import Biologist
from project import Geodesist
from project import Meteorologist
from project import Planet
from project import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.__create_astronaut(astronaut_type, name)

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")

        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astronauts = self.astronaut_repository.find_astronauts_for_mission(5, 30)
        if not astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_count = 0
        for astronaut in astronauts:
            if len(planet.items) == 0:
                break

            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            astronauts_count += 1

        if len(planet.items) == 0:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. " \
                   f"{astronauts_count} astronauts participated in collecting items."
        self.failed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n"
        result += f"{self.failed_missions} missions were not completed!\n"
        result += f"Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut) + "\n"

        return result.strip()

    @staticmethod
    def __create_astronaut(astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")
