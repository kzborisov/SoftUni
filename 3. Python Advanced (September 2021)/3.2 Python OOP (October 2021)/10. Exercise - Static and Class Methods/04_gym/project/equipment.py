class Equipment:
    _id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        res = Equipment._id
        Equipment._id += 1
        return res


    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
