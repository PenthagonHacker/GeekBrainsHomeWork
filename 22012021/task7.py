class ComplexNumber(complex):
    def __init__(self, complex_number):
        super().__init__()
        self.complex_number = complex_number

    def __add__(self, other):
        print('Формула для проверки: (a+bi)+(c+di)=(a+c)+(b+d)i')
        return self + other

    def __mul__(self, other):
        print('Формула для проверки: (a+bi)(c+di)=(ac−bd)+(ad+bc)i')
        return self * other


x = -3 + 4j
y = 2 - 3j

print(x + y, '<=== Сложение | Умножение ===>', x * y)
