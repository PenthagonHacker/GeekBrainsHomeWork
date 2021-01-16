from abc import ABC, abstractmethod


class Clothing(ABC):

    @abstractmethod
    def calculate_fabric(self):
        return 'This method should be overwritten'


class Coat(Clothing):

    def __init__(self, v):
        self.size = v

    @property
    def calculate_fabric(self):
        fabric = self.size / 6.5 + 0.5
        return f'You\'ll need {fabric:.2f} fabric'


class Costume(Clothing):

    def __init__(self, h):
        self.height = h

    @property
    def calculate_fabric(self):
        fabric = self.height * 2 + 0.3
        return f'You\'ll need {fabric} fabric'


# todo реализовать общий подсчёт ткани.


coat = Coat(4)
costume = Costume(1.85)

print(coat.calculate_fabric, '\n', costume.calculate_fabric)
