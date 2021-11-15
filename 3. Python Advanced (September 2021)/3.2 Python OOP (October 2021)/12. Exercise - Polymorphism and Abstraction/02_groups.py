class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    @staticmethod
    def __get_members(members):
        return ", ".join([str(p) for p in members])

    def __add__(self, other):
        name = f"{self.name} {other.name}"
        return Group(name, self.people + other.people)

    def __str__(self):
        members = self.__get_members(self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, item):
        return f"Person {item}: {str(self.people[item])}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
