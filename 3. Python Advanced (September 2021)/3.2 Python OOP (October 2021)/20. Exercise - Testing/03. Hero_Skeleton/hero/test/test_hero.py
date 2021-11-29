import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    username = "Hero"
    level = 10
    health = 100
    damage = 10

    def test_hero_initialization(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        self.assertEqual(self.username, hero.username)
        self.assertEqual(self.level, hero.level)
        self.assertEqual(self.health, hero.health)
        self.assertEqual(self.damage, hero.damage)

    def test_battle__when_username_is_the_same__expect_exception(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero(self.username, self.level, self.health, self.damage)
        expected = "You cannot fight yourself"

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(expected, str(context.exception))

    def test_battle__when_hero_health_is_negative__expected_exception(self):
        hero = Hero(self.username, self.level, -1, self.damage)
        enemy = Hero("enemy", self.level, self.health, self.damage)
        expected = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(expected, str(context.exception))

    def test_battle__when_hero_health_is_zero__expected_exception(self):
        hero = Hero(self.username, self.level, 0, self.damage)
        enemy = Hero("enemy", self.level, self.health, self.damage)
        expected = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(expected, str(context.exception))

    def test_battle__when_enemy_health_is_zero__expected_exception(self):
        enemy_name = "enemy"
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero(enemy_name, self.level, 0, self.damage)
        expected = f"You cannot fight {enemy_name}. He needs to rest"

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(expected, str(context.exception))

    def test_battle__when_enemy_health_is_negative__expected_exception(self):
        enemy_name = "enemy"
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero(enemy_name, self.level, -1, self.damage)
        expected = f"You cannot fight {enemy_name}. He needs to rest"

        with self.assertRaises(Exception) as context:
            hero.battle(enemy)

        self.assertEqual(expected, str(context.exception))

    def test_battle__when_hero_and_enemy_health_is_zero__expected_draw(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        enemy = Hero("enemy", self.level, self.health, self.damage)
        damage = self.damage * self.level
        expected = f"Draw"
        actual = hero.battle(enemy)
        self.assertEqual(self.health - damage, hero.health)
        self.assertEqual(self.health - damage, enemy.health)
        self.assertEqual(expected, actual)

    def test_battle__when_hero_and_enemy_health_is_negative__expected_draw(self):
        hero = Hero(self.username, self.level, self.health, 50)
        enemy = Hero("enemy", self.level, self.health, 50)
        damage = hero.damage * self.level
        expected = f"Draw"
        actual = hero.battle(enemy)
        self.assertEqual(self.health - damage, hero.health)
        self.assertEqual(self.health - damage, enemy.health)
        self.assertEqual(expected, actual)

    def test_battle__when_enemy_health_is_negative__expected_win(self):
        hero = Hero(self.username, 10, 1000, 20)
        enemy = Hero("enemy", 10, 100, 50)
        expected = f"You win"
        actual = hero.battle(enemy)
        self.assertEqual(expected, actual)
        self.assertEqual(11, hero.level)
        self.assertEqual(1000 - 10 * 50 + 5, hero.health)
        self.assertEqual(20 + 5, hero.damage)

    def test_battle__when_enemy_health_is_more_than_zero__expected_win(self):
        hero = Hero(self.username, 10, 1000, 50)
        enemy = Hero("enemy", 10, 1000, 10)
        expected = f"You lose"
        actual = hero.battle(enemy)
        self.assertEqual(expected, actual)
        self.assertEqual(11, enemy.level)
        self.assertEqual(1000 - 10 * 50 + 5, enemy.health)
        self.assertEqual(10 + 5, enemy.damage)

    def test_str(self):
        hero = Hero(self.username, self.level, self.health, self.damage)
        expected = f"Hero {self.username}: {self.level} lvl\n" \
                   f"Health: {self.health}\n" \
                   f"Damage: {self.damage}\n"
        self.assertEqual(expected, str(hero))


if __name__ == "__main__":
    unittest.main()
