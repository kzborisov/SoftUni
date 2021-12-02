from project.baked_food.bread import Bread
from project.bakery import Bakery
from project.drink.tea import Tea
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table

# table = Table(1, 10)
# table.order_food(Bread("Bread", 10))
# table.order_drink(Tea("Tea", 1, "Tea brand!"))
# print(table.get_bill())
# i = InsideTable(50, 10)
# o = OutsideTable(100, 10)
# print(i)
# print(o)
bakery = Bakery("bakery")
bakery.add_food("Cake", "cake_name", 10)
# bakery.add_food("Cak123132e", "dasda", 10)
# bakery.add_food("Cake", "cake_name", 10)

print(bakery.food_menu)
bakery.add_drink("Tea", "tea_name", 10, "tea brand")
bakery.add_drink("Water", "water_name", 10, "water brand")
print(bakery.drinks_menu)
bakery.add_table("InsideTable", 10, 10)
# bakery.add_table("InsideTable", 10, 10)
print(bakery.tables_repository)
print(bakery.tables_repository[0].is_reserved)

print(bakery.reserve_table(11))
print(bakery.tables_repository[0].is_reserved)

print(bakery.reserve_table(1))
print(bakery.tables_repository[0].is_reserved)

