class reverse_iter_iterator:
    def __init__(self, reverse_iter):
        self.reverse_iter = reverse_iter
        self.index = len(self.reverse_iter.iterable) - 1

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.reverse_iter.iterable[self.index]
        self.index -= 1
        return value


class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        return reverse_iter_iterator(self)


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
