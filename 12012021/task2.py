from collections import defaultdict


string = 1
count = defaultdict(str)
with open('task2.txt') as task2:
    string_amount = len(task2.readlines())
    task2.seek(0)
    for line in task2.readlines():
        count.update({f'Строка №{string}': f'Количество слов в строке = {len(line.split())}'})
        string += 1
print(f'Колличество строк в файле: {string_amount}', end='\n============================')
print('\n', dict(count))
