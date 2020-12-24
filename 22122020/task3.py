# Решение с помощью словаря

calendar = {
    'Зима': (12, 1, 2),
    'Весна': (3, 4, 5),
    'Лето': (6, 7, 8),
    'Осень': (9, 10, 11)
}

number = int(input('Введите номер месяца: '))

if 1 <= number <= 12:
    for season, month in calendar.items():
        if number in month:
            print(season)
else:
    print('Введите целое число от 1 до 12')


# Решение с помощью списка

calendar = [('Зима', (12, 1, 2)), ('Весна', (3, 4, 5)), ('Лето', (6, 7, 8)), ('Осень', (9, 10, 11))]

number = int(input('Введите номер месяца: '))

if 1 <= number <= 12:
    for season, month in calendar:
        if number in month:
            print(season)
else:
    print('Введите целое число от 1 до 12')

