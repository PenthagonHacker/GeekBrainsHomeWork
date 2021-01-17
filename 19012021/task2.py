from abc import ABC, abstractmethod


class Clothing(ABC):

    @abstractmethod
    def calculate_fabric(self):
        return 'This method should be overwritten'

    @abstractmethod
    def calculate_fabric_total(self):
        return 'This method should be overwritten'


class Costume(Clothing):
    __count = 0  # счётчик сшитых костюмов
    __fabric_costume_total = []  # список материи, потраченной на каждый костюм

    def __init__(self, h):
        self.height = h
        self.__fabric_costume = self.height * 2 + 0.3
        self.__fabric_costume_total.append(self.__fabric_costume)
        Costume.__count += 1

    @property
    def calculate_fabric(self):  # подсчёт кол-ва ткани на один костюм
        return self.__fabric_costume

    @classmethod  # подсчёт общего кол-ва ткани, затраченной на все костюмы
    def calculate_fabric_total(cls):
        return round(sum(cls.__fabric_costume_total), 2)

    @classmethod  # подсчёт кол-ва костюмов
    def count_costumes(cls):
        return cls.__count


class Coat(Clothing):
    __count = 0  # счётчик сшитых пальто
    __fabric_coat_total = []  # список материи, потраченной на каждое пальто

    def __init__(self, v):
        self.size = v
        self.__fabric_coat = round(self.size / 6.5 + 0.5, 2)
        self.__fabric_coat_total.append(self.__fabric_coat)
        Coat.__count += 1

    @property
    def calculate_fabric(self):  # подсчёт кол-ва ткани на одно пальто
        return self.__fabric_coat

    @classmethod  # подсчёт общего кол-ва ткани, затраченной на все пальто
    def calculate_fabric_total(cls):
        return round(sum(cls.__fabric_coat_total), 2)

    @classmethod  # подсчёт кол-ва пальто
    def count_coats(cls):
        return cls.__count


class FabricTotalAmount:  # класс-контейнер, в котором реализуется общий подсчёт использованной ткани.
    @staticmethod
    def calculate_total_amount():
        return {'Кол-во сшитых костюмов': Costume.count_costumes(),
                'Кол-во сшитых пальто': Coat.count_coats(),
                'Общее кол-во израсходованной материи': round(
                    Costume.calculate_fabric_total() + Coat.calculate_fabric_total(), 2)
                }


costume = Costume(1.85)
costume1 = Costume(2.3)
costume2 = Costume(3.17)
costume3 = Costume(4.56)
print(Costume.calculate_fabric_total())
print(costume2.calculate_fabric)
print(Costume.count_costumes())
# print(costume.__dict__)

coat = Coat(1.85)
coat1 = Coat(2.3)
coat2 = Coat(3.17)
print(Coat.calculate_fabric_total())
print(coat2.calculate_fabric)
print(Coat.count_coats())
# print(coat.__dict__)

fabric_total_amount = FabricTotalAmount()

print(fabric_total_amount.calculate_total_amount())
