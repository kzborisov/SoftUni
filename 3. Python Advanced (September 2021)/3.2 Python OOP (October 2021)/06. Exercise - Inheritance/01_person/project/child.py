from project.person import Person


class Child(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
