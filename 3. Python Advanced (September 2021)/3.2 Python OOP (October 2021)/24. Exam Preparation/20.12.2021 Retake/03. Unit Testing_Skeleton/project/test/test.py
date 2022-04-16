from project.movie import Movie

import unittest


class MovieTests(unittest.TestCase):
    def test_movie_initialization(self):
        movie = Movie("Movie", 1887, 9)
        self.assertEqual("Movie", movie.name)
        self.assertEqual(1887, movie.year)
        self.assertEqual(9, movie.rating)
        self.assertEqual([], movie.actors)

    def test_movie_initialization__when_invalid_name__expected_error(self):
        with self.assertRaises(ValueError) as context:
            Movie("", 2020, 9)

        expected = "Name cannot be an empty string!"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_movie_initialization__when_invalid_year__expected_error(self):
        with self.assertRaises(ValueError) as context:
            Movie("Movie", 1886, 9)

        expected = "Year is not valid!"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_add_actor__when_name_not_added__expected_to_add_actor(self):
        actor_name = "Actor"
        movie = Movie("Movie", 2020, 9)
        movie.add_actor(actor_name)
        self.assertEqual(1, len(movie.actors))
        self.assertEqual(actor_name, movie.actors[0])

    def test_add_actor__when_name_already_added__expected_return_message(self):
        actor_name = "Actor"
        movie = Movie("Movie", 2020, 9)
        movie.add_actor(actor_name)
        actual = movie.add_actor(actor_name)
        expected = f"{actor_name} is already added in the list of actors!"
        self.assertEqual(1, len(movie.actors))
        self.assertEqual(actor_name, movie.actors[0])
        self.assertEqual(expected, actual)

    def test_gt__when_first_rating_is_more(self):
        movie1 = Movie("Movie1", 2020, 10)
        movie2 = Movie("Movie2", 2020, 9)
        expected = f'"{movie1.name}" is better than "{movie2.name}"'
        actual = movie1 > movie2
        self.assertEqual(expected, actual)

    def test_lt__when_first_rating_is_more(self):
        movie1 = Movie("Movie1", 2020, 10)
        movie2 = Movie("Movie2", 2020, 9)
        expected = f'"{movie1.name}" is better than "{movie2.name}"'
        actual = movie1 < movie2
        self.assertEqual(expected, actual)

    def test_gt__when_second_rating_is_more(self):
        movie1 = Movie("Movie1", 2020, 9)
        movie2 = Movie("Movie2", 2020, 10)
        expected = f'"{movie2.name}" is better than "{movie1.name}"'
        actual = movie1 > movie2
        self.assertEqual(expected, actual)

    def test_lt__when_second_rating_is_more(self):
        movie1 = Movie("Movie1", 2020, 9)
        movie2 = Movie("Movie2", 2020, 10)
        expected = f'"{movie2.name}" is better than "{movie1.name}"'
        actual = movie1 < movie2
        self.assertEqual(expected, actual)

    def test_gt__when_rating_is_equal(self):
        movie1 = Movie("Movie1", 2020, 9)
        movie2 = Movie("Movie2", 2020, 9)
        expected = f'"{movie2.name}" is better than "{movie1.name}"'
        actual = movie1 > movie2
        self.assertEqual(expected, actual)

    def test_lt__when__rating_is_equal(self):
        movie1 = Movie("Movie1", 2020, 9)
        movie2 = Movie("Movie2", 2020, 9)
        expected = f'"{movie1.name}" is better than "{movie2.name}"'
        actual = movie1 < movie2
        self.assertEqual(expected, actual)

    def test_repr(self):
        movie = Movie("Movie1", 2020, 9.0)
        movie.add_actor("actor 1")
        movie.add_actor("actor 2")
        expected = f"Name: {movie.name}\n" \
                   f"Year of Release: {movie.year}\n" \
                   f"Rating: {movie.rating:.2f}\n" \
                   f"Cast: {', '.join(movie.actors)}"
        actual = repr(movie)
        self.assertEqual(expected, actual)
        self.assertTrue(isinstance(movie.rating, float))


if __name__ == "__main__":
    unittest.main()
