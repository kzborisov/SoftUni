from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class FoodFactory:
    @staticmethod
    def create_food(food_type, name, price):
        if food_type == Bread.__name__:
            return Bread(name, price)
        if food_type == Cake.__name__:
            return Cake(name, price)


class DrinksFactory:
    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        if drink_type == Tea.__name__:
            return Tea(name, portion, brand)
        if drink_type == Water.__name__:
            return Water(name, portion, brand)


class TableFactory:
    @staticmethod
    def create_table(table_type, table_number, capacity):
        if table_type == InsideTable.__name__:
            return InsideTable(table_number, capacity)
        if table_type == OutsideTable.__name__:
            return OutsideTable(table_number, capacity)


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu: list[BakedFood] = []
        self.drinks_menu: list[Drink] = []
        self.tables_repository: list[Table] = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        # food = FoodFactory.create_food(food_type, name, price)
        food = self.__create_food(food_type, name, price)
        if not food:
            return

        if self.__already_added(name, self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        # drink = DrinksFactory.create_drink(drink_type, name, portion, brand)
        drink = self.__create_drink(drink_type, name, portion, brand)
        if not drink:
            return

        if self.__already_added(name, self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        # table = TableFactory.create_table(table_type, table_number, capacity)
        table = self.__create_table(table_type, table_number, capacity)

        if not table:
            return

        if self.__table_already_exists(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity > number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args: str):
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered = []
        not_ordered = []

        for food_name in args:
            food = self.__get_food_by_name(food_name)
            if not food:
                not_ordered.append(food_name)
                continue

            ordered.append(food)
            table.order_food(food)

        nl = "\n"
        return f"Table {table_number} ordered:\n" \
               f"{nl.join([repr(x) for x in ordered])}\n" \
               f"{self.name} does not have in the menu:\n" \
               f"{nl.join([x for x in not_ordered])}"

    def order_drink(self, table_number: int, *args: str):
        table = self.__get_table_by_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered = []
        not_ordered = []

        for drink_name in args:
            drink = self.__get_drinks_by_name(drink_name)
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
        table = self.__get_table_by_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f'''Table: {table_number}
Bill: {table_bill:.2f}'''

    def get_free_tables_info(self):
        table_infos = [t.free_table_info() for t in self.tables_repository]
        return "\n".join(table_infos)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @staticmethod
    def __create_food(food_type, name, price):
        if food_type == Bread.__name__:
            return Bread(name, price)
        if food_type == Cake.__name__:
            return Cake(name, price)

    @staticmethod
    def __already_added(name, menu_to_check):
        for obj in menu_to_check:
            if obj.name == name:
                return True
        return False

    @staticmethod
    def __create_drink(drink_type, name, portion, brand):
        if drink_type == Tea.__name__:
            return Tea(name, portion, brand)
        if drink_type == Water.__name__:
            return Water(name, portion, brand)

    @staticmethod
    def __create_table(table_type, table_number, capacity):
        if table_type == InsideTable.__name__:
            return InsideTable(table_number, capacity)
        if table_type == OutsideTable.__name__:
            return OutsideTable(table_number, capacity)

    def __table_already_exists(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return True
        return False

    def __get_table_by_number(self, table_number):
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        return tables[0] if tables else None

    def __get_food_by_name(self, name):
        foods = [f for f in self.food_menu if f.name == name]
        return foods[0] if foods else None

    def __get_drinks_by_name(self, name):
        drink = [d for d in self.drinks_menu if d.name == name]
        return drink[0] if drink else None
