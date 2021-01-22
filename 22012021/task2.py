class MyOwnException(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    num, denom = map(int, input('Введите числитель и знаменатель:  ').split())
    if denom == 0:
        raise MyOwnException('Делить на ноль нельзя')
except ValueError:
    print('Вы ввели не число')
except MyOwnException as moe:
    print(moe)
else:
    print(f'Результат деления введённых вами чисел равен  {round(num / denom, 3)}')
