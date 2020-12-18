a = int(input('Введите начальный результат: '))
b = int(input('Введите желаемый результат: '))
day = 1

while True:
    a = a + a * 0.1
    day += 1
    if a >= b:
        break

print(f'Желаемый результат будет достигнут на {day}й день')
