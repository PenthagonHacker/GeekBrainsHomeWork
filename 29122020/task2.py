from random import randrange

lst = [randrange(1, 100) for _ in range(11)]
lst_new = [lst[i + 1] for i in range(len(lst) - 1) if lst[i + 1] > lst[i]]

print(f" Начальный список: {lst}\n Список после преобразований: {lst_new}")
