class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class UpperCaseFormatter(Formatter):
    def format(self, book: Book) -> str:
        return super().format(book).upper()


class TrimCountCharsFormatter(Formatter):
    def __init__(self, count):
        self.count = count

    def format(self, book: Book) -> str:
        return super().format(book)[self.count:]


class Printer:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


b = Book("Hello World")
regular_formater = Formatter()
uppercase_formatter = UpperCaseFormatter()
trim_formatter = TrimCountCharsFormatter(3)

uppercase_printer = Printer(uppercase_formatter)
regular_printer = Printer(regular_formater)
trim_printer = Printer(trim_formatter)

print(regular_printer.get_book(b))
print(uppercase_printer.get_book(b))
print(trim_printer.get_book(b))
