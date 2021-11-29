import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    fuel = 100
    horse_power = 200

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)

    def test_vehicle_str__expect_proper_string(self):
        actual = str(self.vehicle)
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected, actual)

    def test_drive__when_enough_fuel__expected_exception(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__when_not_enough_fuel__expected_decreased_fuel(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption
        self.vehicle.drive(max_distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel__when_too_much_fuel__expected_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)

        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_valid_fuel__expected_increased_fuel(self):
        distance = 10
        self.vehicle.drive(distance)
        consumed_fuel = distance * self.vehicle.fuel_consumption

        expected = self.vehicle.fuel + consumed_fuel
        self.vehicle.refuel(consumed_fuel)
        self.assertEqual(expected, self.vehicle.fuel)


if __name__ == '__main__':
    unittest.main()
