import unittest

# from project.library import Library
from project.library import Library


class TestLibrary(unittest.TestCase):
    name = "test"
    books_by_authors = {}
    readers = {}

    def setUp(self) -> None:
        self.library = Library(self.name)

    def test_library_initialization(self):
        self.assertEqual(self.name, self.library.name)
        self.assertEqual(self.books_by_authors, self.library.books_by_authors)
        self.assertEqual(self.readers, self.library.readers)

    def test_library_raises_error_when_empty_string(self):
        with self.assertRaises(ValueError) as context:
            library = Library("")

        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book__should_add_author_and_title(self):
        author = "Author"
        first_title = "title1"
        secod_title = "title2"
        self.library.add_book(author, first_title)
        self.library.add_book(author, first_title)
        self.library.add_book(author, secod_title)

        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue(author in self.library.books_by_authors)
        self.assertEqual([first_title, secod_title], self.library.books_by_authors[author])

    def test_add_reader__should_add_the_reader(self):
        reader = "reader"
        self.library.add_reader(reader)

        self.assertEqual(1, len(self.library.readers))
        self.assertTrue(reader in self.library.readers)
        self.assertEqual([], self.library.readers[reader])

    def test_add_reader__should_return_error__when_reader_is_the_same(self):
        reader = "reader"
        self.library.add_reader(reader)
        result = self.library.add_reader(reader)
        self.assertEqual(
            f"{reader} is already registered in the {self.library.name} library.",
            result
        )

    def test_rent_book__should_return_error__when_reader_is_not_registered(self):
        result = self.library.rent_book("reader", "author", "title")
        self.assertEqual(f"reader is not registered in the {self.library.name} Library.", result)

    def test_rent_book__should_return_error__when_author_is_not_registered(self):
        author = "author"
        reader = "reader"
        self.library.add_reader(reader)
        result = self.library.rent_book(reader, author, "title")
        self.assertEqual(f"{self.library.name} Library does not have any {author}'s books.", result)

    def test_rent_book__should_return_error__when_title_is_not_registered(self):
        author = "author"
        reader = "reader"
        title = "title"
        self.library.add_reader(reader)
        self.library.add_book(author, "random title")
        result = self.library.rent_book(reader, author, title)
        self.assertEqual(f"""{self.library.name} Library does not have {author}'s "{title}".""", result)

    def test_rent_book__should_properly_rent_book(self):
        author = "author"
        reader = "reader"
        first_title = "title"
        second_title = "title2"
        self.library.add_reader(reader)
        self.library.add_book(author, first_title)
        self.library.add_book(author, second_title)
        self.library.rent_book(reader, author, first_title)

        self.assertEqual(1, len(self.library.books_by_authors[author]))
        self.assertEqual([{author: first_title}], self.library.readers[reader])
        self.assertTrue(first_title not in self.library.books_by_authors[author])
        self.assertTrue(second_title in self.library.books_by_authors[author])


if __name__ == '__main__':
    unittest.main()
