class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 3000, 'bonus': 1000}


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str):   # поскольку в данном случае инициализатор дочернего класса
        super().__init__(name, surname, position)  # полностью совпадает с родительским, то можно было опустить эти две строки...

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pos = Position('Bilbo', 'Baggins', 'Hobbit')

print(pos.get_full_name(), pos.get_total_income())
