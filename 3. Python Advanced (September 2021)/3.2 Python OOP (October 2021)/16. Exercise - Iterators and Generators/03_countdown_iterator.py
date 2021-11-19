class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 0:
            raise StopIteration()

        i = self.i
        self.i -= 1
        return i


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")
