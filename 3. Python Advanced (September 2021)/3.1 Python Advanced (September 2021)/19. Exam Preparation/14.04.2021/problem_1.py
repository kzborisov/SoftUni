import sys
from collections import deque
from io import StringIO


# test_input = """11, 6, 8, 1
# 3, 1, 9, 10, 5, 9, 1"""
#
# test_input_2 = """10, 9, 8, 7, 5
# 5, 10, 9, 8, 7"""
# test_input_3 = """12, -3, 14, 3, 2, 0
# 10, 15, 4, 6, 3, 1, 22, 1"""
#
# sys.stdin = StringIO(test_input)
# sys.stdin = StringIO(test_input_2)
# sys.stdin = StringIO(test_input_3)

def read_input():
    return (list(map(int, input().split(", "))),
            list(map(int, input().split(", "))))


def is_order_valid(order):
    return order in range(1, 11)


def print_result(pizza_orders, employees, total_pizzas):
    if not pizza_orders:
        print("All orders are successfully completed!")
        print(f"Total pizzas made: {total_pizzas}")
        print(f"Employees: {', '.join(str(x) for x in employees)}")
    else:
        print("Not all orders are completed.")
        print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")


orders, employees = read_input()
orders = deque(orders)
total_pizzas = 0

while orders and employees:
    if not is_order_valid(orders[0]):
        orders.popleft()
        continue

    order = orders.popleft()
    employee_capacity = employees.pop()

    if order > employee_capacity:
        remaining_pizzas = order - employee_capacity
        total_pizzas += employee_capacity
        orders.appendleft(remaining_pizzas)
        continue

    total_pizzas += order

print_result(orders, employees, total_pizzas)
