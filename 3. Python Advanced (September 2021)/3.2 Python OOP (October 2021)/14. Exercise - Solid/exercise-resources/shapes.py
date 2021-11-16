from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def calc_area(self):
        return self.height * self.side / 2


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    @property
    def shapes(self):
        return self._shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("`shapes` should be of type `list`.")
        self._shapes = value

    @property
    def total_area(self):
        return sum([shape.calc_area() for shape in self.shapes])


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
