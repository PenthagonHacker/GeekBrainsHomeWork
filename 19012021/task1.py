class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        import numpy as np
        m = np.array(self.lst)
        return '\n'.join(str(r) for r in m)

    def __add__(self, other):
        import numpy as np
        return Matrix(np.array(self.lst) + np.array(other.lst))


matrix = Matrix([[1, 2, 3], [4, 5, 6]])
matrix1 = Matrix([[11, 22, 33], [44, 55, 66]])

print(matrix, '\n')
print(matrix1, '\n')
print(matrix + matrix1)
