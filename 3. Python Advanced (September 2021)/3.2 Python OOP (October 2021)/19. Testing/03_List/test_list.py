from extended_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):
    def test_init__when_integers__expected_valid_data(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(3, len(integer_list.get_data()))

    def test_init__when_not_integers__expected_no_elements(self):
        integer_list = IntegerList("a", "b", "c")
        self.assertEqual(0, len(integer_list.get_data()))

    def test_add__when_integer__expected_to_return_the_list(self):
        integer_list = IntegerList(1, 2, 3)
        expected = [1, 2, 3, 4]
        actual = integer_list.add(4)

        self.assertEqual(expected, actual)

    def test_add__when_not_integer__expected_exception(self):
        integer_list = IntegerList(1, 2, 3)
        expected = "Element is not Integer"
        with self.assertRaises(ValueError) as context:
            integer_list.add("blahbla")

        self.assertEqual(expected, str(context.exception))

    def test_remove_index__when_valid_index__expected_to_remove_element_and_return_value(self):
        integer_list = IntegerList(1, 2, 3)
        valid_index = 2
        expected_value = 3
        actual_value = integer_list.remove_index(valid_index)

        self.assertEqual(2, len(integer_list.get_data()))
        self.assertEqual(expected_value, actual_value)

    def test_remove_index__when_valid_index__expected_exception(self):
        integer_list = IntegerList(1, 2, 3)
        invalid_index = 3
        expected = "Index is out of range"
        with self.assertRaises(Exception) as context:
            integer_list.remove_index(invalid_index)

        self.assertEqual(expected, str(context.exception))

    def test_get__when_valid_index__expected_get_data(self):
        integer_list = IntegerList(1, 2, 3)
        valid_index = 2
        expected_value = 3
        actual_value = integer_list.get(valid_index)

        self.assertEqual(expected_value, actual_value)

    def test_get__when_invalid_index__expected_exception(self):
        integer_list = IntegerList(1, 2, 3)
        invalid_index = 3
        expected = "Index is out of range"
        with self.assertRaises(Exception) as context:
            integer_list.get(invalid_index)

        self.assertEqual(expected, str(context.exception))

    def test_insert__when_valid_index_and_valid_elements__expected_to_add_to_list(self):
        integer_list = IntegerList(1, 2, 3)
        valid_index = 2
        valid_element = 4
        integer_list.insert(valid_index, valid_element)

        self.assertEqual(4, len(integer_list.get_data()))

    def test_insert__when_invalid_index_and_valid_elements__expected_exception(self):
        integer_list = IntegerList(1, 2, 3)
        valid_index = 3
        valid_element = 4
        expected_exception = "Index is out of range"
        with self.assertRaises(Exception) as context:
            integer_list.insert(valid_index, valid_element)

        self.assertEqual(expected_exception, str(context.exception))

    def test_insert__when_valid_index_and_invalid_elements__expected_exception(self):
        integer_list = IntegerList(1, 2, 3)
        valid_index = 2
        valid_element = "invalid element"
        expected_exception = "Element is not Integer"
        with self.assertRaises(Exception) as context:
            integer_list.insert(valid_index, valid_element)

        self.assertEqual(expected_exception, str(context.exception))

    def test_get_biggest__expected_biggest_value_of_data(self):
        integer_list = IntegerList(1, 2, 3)
        expected = 3
        actual = integer_list.get_biggest()
        self.assertEqual(expected, actual)

    def test_get_index__when_valid_element__expected_element_index(self):
        integer_list = IntegerList(1, 2, 3)
        expected = 2
        element = 3
        actual = integer_list.get_index(element)
        self.assertEqual(expected, actual)

    def test_get_index__when_invalid_element__expected(self):
        integer_list = IntegerList(1, 2, 3)
        expected = "5 is not in list"
        element = 5
        with self.assertRaises(ValueError) as context:
            integer_list.get_index(element)
        self.assertEqual(expected, str(context.exception))


if __name__ == '__main__':
    unittest.main()
