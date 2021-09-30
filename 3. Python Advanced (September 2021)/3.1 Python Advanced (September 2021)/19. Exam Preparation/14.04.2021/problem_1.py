from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacities = [int(x) for x in input().split(", ")]

completed = True
total_pizzas_count = 0

while True:
    if not pizza_orders:
        break

    if pizza_orders[0] <= 0 or pizza_orders[0] > 10:
        pizza_orders.popleft()
        continue

    first_pizza_order = pizza_orders.popleft()
    last_employee_capacity = employees_capacities.pop()

    if first_pizza_order <= last_employee_capacity:
        total_pizzas_count += first_pizza_order
        continue
    elif first_pizza_order > last_employee_capacity:
        total_pizzas_count += last_employee_capacity
        pizza_orders.appendleft((first_pizza_order - last_employee_capacity))
        if not employees_capacities:
            completed = False
            break

if completed:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_count}")
    print(f"Employees: {', '.join(str(x) for x in employees_capacities)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
