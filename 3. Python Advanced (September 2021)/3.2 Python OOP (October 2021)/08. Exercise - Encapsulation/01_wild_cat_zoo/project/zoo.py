class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.budget < price:
            return "Not enough budget"

        if len(self.animals) >= self.animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{current_worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_paycheck = sum([x.salary for x in self.workers])
        if total_paycheck > self.budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.budget -= total_paycheck
        return f"You payed your workers. They are happy. Budget left: {self.budget}"

    def tend_animals(self):
        total_cost = sum([x.money_for_care for x in self.animals])
        if total_cost > self.budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.budget -= total_cost
        return f"You tended all the animals. They are happy. Budget left: {self.budget}"

    def profit(self, amount):
        self.budget += amount

    def __get_type(self, animal):
        return animal.__class__.__name__

    def __count_animals(self, animal_type):
        return len([x for x in self.animals if self.__get_type(x) == animal_type])

    def __count_workers(self, worker_type):
        return len([x for x in self.workers if self.__get_type(x) == worker_type])

    def animals_status(self):
        status = f"You have {len(self.animals)} animals\n"
        status += f"----- {self.__count_animals('Lion')} Lions:\n"
        status += "\n".join([str(x) for x in self.animals if self.__get_type(x) == 'Lion'])

        status += f"\n----- {self.__count_animals('Tiger')} Tigers:\n"
        status += "\n".join([str(x) for x in self.animals if self.__get_type(x) == 'Tiger'])

        status += f"\n----- {self.__count_animals('Cheetah')} Cheetahs:\n"
        status += "\n".join([str(x) for x in self.animals if self.__get_type(x) == 'Cheetah'])
        return status

    def workers_status(self):
        status = f"You have {len(self.workers)} workers\n"
        status += f"----- {self.__count_workers('Keeper')} Keepers:\n"
        status += "\n".join([str(x) for x in self.workers if self.__get_type(x) == 'Keeper'])

        status += f"\n----- {self.__count_workers('Caretaker')} Caretakers:\n"
        status += "\n".join([str(x) for x in self.workers if self.__get_type(x) == 'Caretaker'])

        status += f"\n----- {self.__count_workers('Vet')} Vets:\n"
        status += "\n".join([str(x) for x in self.workers if self.__get_type(x) == 'Vet'])
        return status

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value
