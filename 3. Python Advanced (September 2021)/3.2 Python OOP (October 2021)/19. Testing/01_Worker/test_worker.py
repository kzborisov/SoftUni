from worker import Worker

import unittest


class WokerTests(unittest.TestCase):
    valid_name = "Worker1"
    valid_salary = 1000
    valid_energy = 5
    valid_money = 0

    def test_init__when_valid__expected_to_initialize(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)
        self.assertEqual(self.valid_money, worker.money)

    def test_rest__when_valid_energy__expected_to_increment_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.rest()
        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_work__when_negative_energy__expected_exception(self):
        worker = Worker(self.valid_name, self.valid_salary, -1)
        expected_exception = "Not enough energy."
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual(expected_exception, str(context.exception))

    def test_work__when_zero_energy__expected_exception(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)
        expected_exception = "Not enough energy."
        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual(expected_exception, str(context.exception))

    def test_work__when_valid_energy_expected_increased_salary(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()

        self.assertEqual(self.valid_salary * 2, worker.money)

    def test_work__when_valid_energy_expected_decreased_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()

        self.assertEqual(self.valid_energy - 1, worker.energy)

    def test_get_info__when_valid__expected_correct_string(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        expected = f'{self.valid_name} has saved {self.valid_money} money.'
        actual = worker.get_info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
