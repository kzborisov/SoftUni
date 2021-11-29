from cat import Cat

import unittest

class CatTests(unittest.TestCase):
    name = "Cat"
    fed = False
    sleepy = False
    size = 0

    def test_eat__when_valid__expected_increased_size(self):
        cat = Cat(self.name)
        cat.eat()

        self.assertEqual(self.size + 1, cat.size)

    def test_eat__when_valid__expected_cat_is_fed(self):
        cat = Cat(self.name)
        cat.eat()
        self.assertNotEqual(self.fed, cat.fed)

    def test_eat__when_already_fed__expected_exception(self):
        cat = Cat(self.name)
        cat.fed = True
        expected_exception = "Already fed."

        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertEqual(expected_exception, str(context.exception))

    def test_sleep__when_not_fed__expected_exception(self):
        cat = Cat(self.name)
        expected_exception = "Cannot sleep while hungry"
        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertEqual(expected_exception, str(context.exception))

    def test_sleep__when_valid__expected_not_sleepy(self):
        cat = Cat(self.name)
        cat.eat()
        cat.sleep()

        self.assertEqual(self.sleepy, cat.sleepy)


if __name__ == '__main__':
    unittest.main()
