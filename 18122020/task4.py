number = int(input('Введите число: '))
max = 0
while number > 10:
    figure = number % 10
    if figure > max:
        max = figure
    number //= 10

print(max)
