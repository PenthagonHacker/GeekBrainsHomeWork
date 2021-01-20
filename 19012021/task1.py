class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return '\n'.join(str(r) for r in self.lst)

    def compatibility_check(self, other):  # проверка на одинаковые размеры матриц
        count = 0
        if len(self.lst) == len(other.lst):
            for elem in self.lst:
                for elem1 in other.lst:
                    if len(elem) != len(elem1):
                        return False
            else:
                return True
        else:
            return False

    def __add__(self, other):
        result = []
        if self.compatibility_check(other):
            for row in range(len(self.lst)):
                for elem in range(len(self.lst[0])):
                    result.append(self.lst[row][elem] + other.lst[row][elem])  # получил сумму соотв. элементов
                    self.result1 = [result[i: i + len(self.lst[0])] for i in
                                    range(0, len(result), len(self.lst[0]))]  # разделил список на списки
        else:
            return f'Данные матрицы складывать нельзя'
        return Matrix(self.result1)


matrix = Matrix([[1, 2, 3], [4, 5, 6]])
matrix1 = Matrix([[11, 22, 33], [44, 55, 66]])

print(matrix, '\n')
print(matrix1, '\n')
print(matrix + matrix1)
