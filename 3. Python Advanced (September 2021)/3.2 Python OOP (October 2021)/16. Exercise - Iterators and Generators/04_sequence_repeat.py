class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == self.number:
            raise StopIteration()

        idx = self.__index
        self.__index += 1
        return self.sequence[idx % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
