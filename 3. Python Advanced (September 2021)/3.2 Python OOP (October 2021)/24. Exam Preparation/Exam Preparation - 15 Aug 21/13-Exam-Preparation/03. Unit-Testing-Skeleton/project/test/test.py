import unittest

from project.pet_shop import PetShop


class TestPetShop(unittest.TestCase):
    def test_pet_shop_initialization(self):
        petshop = PetShop("PetShop")
        self.assertEqual("PetShop", petshop.name)
        self.assertEqual({}, petshop.food)
        self.assertEqual([], petshop.pets)

    def test_add_food__when_quantity_is_negative__expected_value_error(self):
        petshop = PetShop("PetShop")
        with self.assertRaises(ValueError) as context:
            petshop.add_food("food", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food__when_quantity_is_zero__expected_value_error(self):
        petshop = PetShop("PetShop")
        with self.assertRaises(ValueError) as context:
            petshop.add_food("food", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food__when_food_not_added__expected_to_add_with_zero(self):
        petshop = PetShop("PetShop")
        result = petshop.add_food("food", 1)
        self.assertTrue('food' in petshop.food)
        self.assertEqual(1, petshop.food['food'])
        self.assertEqual(f"Successfully added {1:.2f} grams of food.", result)

    def test_add_pet__when_pet_not_add__expected_to_add_pet(self):
        petshop = PetShop("PetShop")
        result = petshop.add_pet("pet")
        self.assertTrue('pet' in petshop.pets)
        self.assertEqual(f"Successfully added pet.", result)

    def test_add_pet__when_pet_added__expected_exception(self):
        petshop = PetShop("PetShop")
        petshop.add_pet('pet')
        with self.assertRaises(Exception) as context:
            petshop.add_pet('pet')

        self.assertEqual("Cannot add a pet with the same name", str(context.exception))
        self.assertEqual(1, len(petshop.pets))

    def test_repr(self):
        petshop = PetShop("PetShop")
        petshop.add_pet("pet")
        expected = f'Shop PetShop:\n' \
                   f'Pets: pet'
        self.assertEqual(expected, repr(petshop))

    def test_feed_pet__when_invalid_pet_name__expected_exception(self):
        petshop = PetShop("PetShop")
        expected = 'Please insert a valid pet name'
        with self.assertRaises(Exception) as context:
            petshop.feed_pet("food", "pet")

        self.assertEqual(expected, str(context.exception))

    def test_feed_pet__when_food_missing__expected_correct_message(self):
        petshop = PetShop("PetShop")
        food_name = 'food'
        pet_name = 'pet'
        petshop.add_pet(pet_name)
        expected = f'You do not have {food_name}'
        result = petshop.feed_pet(food_name, pet_name)

        self.assertEqual(expected, result)

    def test_feed_pet__when_food_less_than_hundred__expected_to_add_food(self):
        petshop = PetShop("PetShop")
        food_name = 'food'
        quantity = 10
        pet_name = 'pet'
        petshop.add_pet(pet_name)
        petshop.add_food(food_name, quantity)
        expected = "Adding food..."
        result = petshop.feed_pet(food_name, pet_name)

        self.assertEqual(1000.00 + quantity, petshop.food[food_name])
        self.assertEqual(expected, result)

    def test_feed_pet__when_food_valid_food__expected_to_feed_pet(self):
        petshop = PetShop("PetShop")
        food_name = 'food'
        quantity = 110
        pet_name = 'pet'
        petshop.add_pet(pet_name)
        petshop.add_food(food_name, quantity)
        expected = f"{pet_name} was successfully fed"
        result = petshop.feed_pet(food_name, pet_name)

        self.assertEqual(quantity - 100, petshop.food[food_name])
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
