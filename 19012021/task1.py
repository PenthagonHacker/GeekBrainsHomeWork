class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return '\n'.join(str(r) for r in self.lst)

    def compatibility_check(self):  # проверка на одинаковые размеры матриц
        pass
        # todo if len(self.lst) == len(other.lst) and something else:
        #       checking
        #        return True
        #     else:
        #        return f'Данные матрицы не подлежат сложению'

    def __add__(self, other):
        result = []
        for row in range(len(self.lst)):
            for elem in range(len(self.lst[0])):
                result.append(self.lst[row][elem] + other.lst[row][elem])  # получил сумму соотв. элементов
                self.result1 = [result[i: i + len(self.lst[0])] for i in
                                range(0, len(result), len(self.lst[0]))]  # разделил список на списки
        return Matrix(self.result1)



matrix = Matrix([[1, 2, 3], [4, 5, 6]])
matrix1 = Matrix([[11, 22, 33], [44, 55, 66]])
#
print(matrix, '\n')
print(matrix1, '\n')
print(matrix + matrix1)


