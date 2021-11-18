class vowels_iterator:
    def __init__(self, vowels):
        self.vowels = vowels
        self.start = 0
        self.end = len(self.vowels.input_string) - 1

    def __is_vowel(self, letter):
        return letter.lower() in ("a", "e", "i", "u", "y", "o")

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        letter = self.vowels.input_string[self.start]
        self.start += 1

        if not self.__is_vowel(letter):
            return self.__next__()
        return letter


class vowels:
    def __init__(self, input_string):
        self.input_string = input_string

    def __iter__(self):
        return vowels_iterator(self)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
