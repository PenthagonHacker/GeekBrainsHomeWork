from collections import defaultdict

structure = []
final_structure = defaultdict(list)
goods = {}
title = ''
price, amount = 0, 0
quantity = 'шт'
i = 1


while True:  # подготовка структуры данных
    try:
        title = input('Введите НАЗВАНИЕ товара. Нажмите CTRL+D после ввода всех необходимых сведений: ')
        price = int(input('Введите ЦЕНУ товара. Нажмите CTRL+D после ввода всех необходимых сведений: '))
        amount = int(input('Введите КОЛЛИЧЕСТВО товара. Нажмите CTRL+D после ввода всех необходимых сведений: '))
        unit = input('Введите ЕД. товара. Нажмите CTRL+D после ввода всех необходимых сведений: ')
        goods['Название'] = title
        goods['Цена'] = price
        goods['Колличество'] = amount
        goods['Ед.'] = unit
        structure.append((i, goods.copy()))
        i += 1
    except EOFError:
        break

# парсинг структуры данных
for elem in structure:
    final_structure['Название'].append(elem[1]['Название'])
    final_structure['Цена'].append(elem[1]['Цена'])
    final_structure['Колличество'].append(elem[1]['Колличество'])
    final_structure['Ед.'].append(elem[1]['Ед.'])

print(dict(final_structure))
