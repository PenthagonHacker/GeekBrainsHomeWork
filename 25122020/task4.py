#первый способ  с помощью знака **

def my_func(x,y):
    if all([x > 0, y <= 0, type(y) == int]):
        if y == 0:
            return f'x = 1'
        return f'x = {x**y}'
    return f'Проверьте правильность вводных данных'



#второй способ

def my_func(x, y):
    result = 1
    if all([x > 0, y <= 0, type(y) == int]):
        if y == 0:
            return f'x = 1'
        while y != 0:
            result *= x
            y += 1
        return f'x = {1 / result}'
    return f'Проверьте правильность вводных данных'


foo = my_func(2, -2)
print(foo)
