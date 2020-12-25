# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    lst = [arg1, arg2, arg3]
    lst.sort(reverse=True)
    return lst[0]+lst[1]

foo = my_func(4,6,1)

print(foo)

#Альтернативный способ

# def my_func(*args):
#     lst = list(args)
#     if len(lst) != 3:
#         return 'Вы ввели не 3 числа! \nПовторите ввод'
#     else:
#         lst.sort(reverse=True)
#         return lst[0] + lst[1]
#
# print(my_func(4,6,9))