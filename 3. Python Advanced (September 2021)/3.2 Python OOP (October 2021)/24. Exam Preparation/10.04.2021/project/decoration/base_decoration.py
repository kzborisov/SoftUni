from abc import abstractmethod, ABC


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price
