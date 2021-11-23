from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread  # noqa
from project.baked_food.cake import Cake  # noqa
from project.drink.drink import Drink
from project.drink.tea import Tea  # noqa
from project.drink.water import Water  # noqa
from project.table.inside_table import InsideTable  # noqa
from project.table.outside_table import OutsideTable  # noqa
from project.table.table import Table


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in ("Bread", "Cake"):
            return

        for f in self.food_menu:
            if f.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        food = globals()[food_type](name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in ("Tea", "Water"):
            return

        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = globals()[drink_type](name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in ("InsideTable", "OutsideTable"):
            return

        for t in self.tables_repository:
            if t.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        table = globals()[table_type](table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.is_reserved:
                continue

            if table.capacity < number_of_people:
                continue

            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args: str):
        try:
            table = [table for table in self.tables_repository if table.table_number == table_number][0]
            unordered_food = []
            ordered_food = []
            for food_name in args:
                try:
                    food = [food for food in self.food_menu if food.name == food_name][0]
                    table.order_food(food)
                    ordered_food.append(food)
                except IndexError:
                    unordered_food.append(food_name)
            ordered_food_list = "\n".join([repr(ordered) for ordered in ordered_food])
            unordered_food_list = "\n".join(unordered_food)
            return f"Table {table_number} ordered:\n" \
                   f"{ordered_food_list}\n" \
                   f"{self.name} does not have in the menu:\n" \
                   f"{unordered_food_list}"

        except IndexError:
            return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *args: str):
        table = self.__find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered = []
        not_ordered = []

        for drink_name in args:
            drink = self.__find_drink(drink_name)
            if not drink:
                not_ordered.append(drink_name)
                continue

            ordered.append(drink)
            table.order_drink(drink)

        nl = "\n"
        return f"Table {table_number} ordered:\n" \
               f"{nl.join([repr(x) for x in ordered])}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{nl.join([x for x in not_ordered])}"

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        table_bill = table.get_bill()
        table.clear()
        self.total_income += table_bill
        return f"Table: {table_number}\n" \
               f"Bill: {table_bill:.2f}"

    def get_free_tables_info(self):
        return "\n".join([table.free_table_info() for table in self.tables_repository])

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def __find_food(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def __find_drink(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink
