class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if not self._has_customer_capacity():
            return

        self.customers.append(customer)

    def add_dvd(self, dvd):
        if not self._has_dvd_capacity():
            return
        self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_object_by_id(self.customers, customer_id)
        dvd = self.__get_object_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if not self.is_allowed_to_rent(customer.age, dvd.age_restriction):
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_object_by_id(self.customers, customer_id)
        dvd = self.__get_object_by_id(self.dvds, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def _has_customer_capacity(self):
        return len(self.customers) < self.customer_capacity()

    def _has_dvd_capacity(self):
        return len(self.dvds) < self.dvd_capacity()

    @staticmethod
    def __get_object_by_id(objects, object_id):
        customers = [x for x in objects if x.id == object_id]
        return customers[0]

    @staticmethod
    def is_allowed_to_rent(customer_age, age_restriction):
        return customer_age >= age_restriction

    def __repr__(self):
        result = '\n'.join([str(x) for x in self.customers]) + "\n"
        result += '\n'.join([str(x) for x in self.dvds])
        return result
