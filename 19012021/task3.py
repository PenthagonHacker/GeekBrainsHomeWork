class Cell:
    def __init__(self, cellule: int):
        self.cellule = cellule
        if not isinstance(self.cellule, int) or self.cellule <= 0:  # проверка на корректность кол-ва введёных ячеек
            exit('Новая клетка не может быть сформированна из-за недостаточного кол-ва ячеек')

    def __add__(self, other):
        return Cell(self.cellule + other.cellule)

    def __sub__(self, other):
        if self.cellule - other.cellule > 0:
            return f'Осталось {self.cellule - other.cellule} ячеек'
        else:
            exit('Resulting amount of cellules is negative')

    def __mul__(self, other):
        return Cell(self.cellule * other.cellule)

    def __truediv__(self, other):
        if isinstance(self.cellule // other.cellule, int):
            return Cell(self.cellule // other.cellule)

    def make_order(self, cellules_in_row):
        rows, rest = divmod(self.cellule, cellules_in_row)
        cellules_string = ('*'*cellules_in_row+r'\n')*rows + '*'*rest
        return cellules_string


    def __str__(self):
        return f'Образована клетка с количеством ячеек: {self.cellule}'


cell = Cell(5)
cell1 = Cell(6)
cell2 = Cell(14)

print(cell + cell1)
print(cell1 - cell)
print(cell * cell1)
print(cell1 / cell)

print(cell2.make_order(3))
