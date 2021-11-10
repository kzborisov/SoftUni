class Category:
    def __init__(self, category_id, name):
        self.id = category_id
        self.name = name

    def edit(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
