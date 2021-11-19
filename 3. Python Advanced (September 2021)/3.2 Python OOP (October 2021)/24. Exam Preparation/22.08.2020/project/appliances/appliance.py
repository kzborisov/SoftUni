class Appliance:
    def __init__(self, cost):
        # for a single day
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * 30
