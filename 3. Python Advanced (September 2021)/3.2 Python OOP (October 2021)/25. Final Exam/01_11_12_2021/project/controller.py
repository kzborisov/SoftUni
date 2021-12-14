from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self, ):
        self.cars: list[Car] = []
        self.drivers: list[Driver] = []
        self.races: list[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.__create_car(car_type, model, speed_limit)
        if not car:
            return

        if self.__is_car_added(model):
            raise Exception(f"Car {model} is already created!")

        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)

        if self.__is_driver_added(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = Race(race_name)
        if self.__is_race_added(race_name):
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_car_by_type(car_type)
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_car = driver.car
            # TODO: Perhaps this is needed
            old_car.is_taken = False
            driver.car = car
            driver.car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        driver.car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for d in race.drivers:
            if d.name == driver_name:
                return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")

        winners = race.get_winners()
        for winner in winners:
            winner.number_of_wins += 1

        msg = [f"Driver {w.name} wins the {race_name} race with a speed of {w.car.speed_limit}."
               for w in winners]
        return "\n".join(msg).strip()


    @staticmethod
    def __create_car(car_type, model, speed_limit):
        if car_type == MuscleCar.__name__:
            return MuscleCar(model, speed_limit)
        if car_type == SportsCar.__name__:
            return SportsCar(model, speed_limit)

    def __is_car_added(self, model):
        for car in self.cars:
            if car.model == model:
                return True
        return False

    def __is_driver_added(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return True
        return False

    def __is_race_added(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return True
        return False

    def __find_driver_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __find_car_by_type(self, car_type):
        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car

    def __find_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
