import json
import os


with open('task7.txt', encoding='utf-8') as task7:
    task7_actual = task7.readlines()[1:]  #читаю файл со строки, следующей за строкой с названиями столбцов.
    lst, dct, = [], {}
    for line in task7_actual:
        dct.update({line.split()[0]: int(line.split()[2]) - int(line.split()[3])}) #создаю словарь с парами имя:прибыль
    x = [profit for profit in dct.values() if profit > 0] #создаю list comprehension, чтобы исключить фирмы с убытками.
    lst.append(dct)
    lst.append({'average_profit': round(sum(x) / len(x), 2)})
with open('task7_json.json', 'w') as task7json:
    json.dump(lst, task7json)
print(f"Файл был успешно сериализован. Вы можете найти его по адресу {os.path.join(os.getcwd(), 'task7_json.json')}")


