def sell_car(car):
    if cars[car][MILEAGE] >= 100000:
        return True
    return False


def drive(car, distance, fuel):
    if cars[car][FUEL] - fuel >= 0:
        cars[car][MILEAGE] += distance
        cars[car][FUEL] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if sell_car(car):
            print(f"Time to sell the {car}!")
            cars.pop(car)
    else:
        print(f"Not enough fuel to make that ride")


def refuel(car, fuel):
    if cars[car][FUEL] + fuel > MAX_FUEL:
        fuel = MAX_FUEL - cars[car][FUEL]

    if fuel > 0:
        cars[car][FUEL] += fuel
        print(f"{car} refueled with {fuel} liters")


def revert(car, kilometers):
    cars[car][MILEAGE] -= kilometers
    if cars[car][MILEAGE] < 10000:
        cars[car][MILEAGE] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


n = int(input())
cars = {}
MILEAGE = "mileage"
FUEL = "fuel"
MAX_FUEL = 75

for _ in range(n):
    curr_car, curr_mileage, curr_fuel = input().split("|")
    if curr_car not in cars:
        cars[curr_car] = {MILEAGE: int(curr_mileage), FUEL: int(curr_fuel)}

command = input()

while not command == "Stop":
    cmd = command.split(" : ")
    if cmd[0] == "Drive":
        curr_car, curr_distance, curr_fuel = cmd[1:]
        drive(curr_car, int(curr_distance), int(curr_fuel))
    elif cmd[0] == "Refuel":
        curr_car, curr_fuel = cmd[1:]
        refuel(curr_car, int(curr_fuel))
    elif cmd[0] == "Revert":
        curr_car, curr_km = cmd[1:]
        revert(curr_car, int(curr_km))

    command = input()

for car, car_info in sorted(cars.items(), key=lambda x: (-x[1][MILEAGE], x[0])):
    print(f"{car} -> Mileage: {car_info[MILEAGE]} kms, Fuel in the tank: {car_info[FUEL]} lt.")
