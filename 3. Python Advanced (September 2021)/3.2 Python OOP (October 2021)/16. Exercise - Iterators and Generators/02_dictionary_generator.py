class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.__data = iter(self.dict.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__data)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
