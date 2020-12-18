income = int(input('Введите выручку фирмы: '))
expends = int(input('Введите издержки фирмы: '))
profit = ((income - expends) / income) * 100

if income >= expends:
    print('Финансовый результат: ПРИБЫЛЬ')
    print('Рентабельность выручки составила {:.4}'.format(profit))
    staff = int(input('Введите кол-во сотрудников: '))
    print('Прибыль фирмы в расчёте на одного сотрудника составляет: {:.3}'.format(profit / staff))

print('Финансовый результат: УБЫТОК')
