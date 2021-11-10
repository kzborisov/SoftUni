class Customer:
    _id = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        res = Customer._id
        Customer._id += 1
        return res

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; " \
               f"Email: {self.email}"
