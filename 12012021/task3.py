from numpy import mean


with open('task3.txt', encoding='utf-8') as task3:
    average, lst = [], []
    for line in task3.readlines():
        if float(line.split()[1]) < 20000:
            lst.append(line.split()[0])
        average.append(float(line.split()[1]))

print(f'Список сотрудников с окладом < 20т.р. : {lst}', end='\n\n')
print(f'Средняя величина дохода сотрудников: {mean(average):.2f}')
