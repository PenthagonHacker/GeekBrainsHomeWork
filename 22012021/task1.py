'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, data: str):
        self.__data = data

    @classmethod
    def data_to_int(cls, obj):
        split_data_to_int = list(map(int, obj.data.split('-')))
        return split_data_to_int

    @staticmethod
    def check_data(obj):
        from time import strptime
        try:
            valid_date = strptime(obj.data.replace('-', '/'), '%d/%m/%Y')
        except ValueError as ve:
            return f'{ve}'
        else:
            return f'Дата введена корректно'


    @property
    def data(self):
        return self.__data


data = Data('11-02-2004')
print(Data.data_to_int(data))
print(data.check_data(data))
