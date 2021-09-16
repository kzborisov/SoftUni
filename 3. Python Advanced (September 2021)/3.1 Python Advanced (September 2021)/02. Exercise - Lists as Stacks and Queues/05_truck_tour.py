from collections import deque

pump_count = int(input())
pumps_queue = deque()

for _ in range(pump_count):
    pump = [int(x) for x in input().split()]
    pumps_queue.append(pump)

for attempt in range(pump_count):
    is_completed = True
    car_fuel = 0
    for petrol, distance in pumps_queue:
        car_fuel += petrol
        if distance > car_fuel:
            is_completed = False
            break
        car_fuel -= distance

    if is_completed:
        print(attempt)
        break

    pumps_queue.append(pumps_queue.popleft())
