from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("name", "mammal_type", "sound")

    def test_init(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("mammal_type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound__expected_propper_string(self):
        expected = f"name makes sound"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info(self):
        expected = "name is of type mammal_type"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
