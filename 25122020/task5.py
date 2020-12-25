def getsum():
    result = 0
    while True:
        if input("Выход 'Q'\n'Enter' - продолжить ").upper() == 'Q':
            break
        string = input('Введите строку чисел, разделенных пробелом (специальный символ "Q"): ').split()  # делаю список из строковых данных, чтобы можно было найти спец.символ
        if 'Q' in string:
            index = string.index('Q')   #В случае если спец. символ найден, ищу его индекс в списке, чтобы обрезать до нужного положения.
            digit_string = list(map(int, string[:index]))  # делаю список чисел, чтобы искать сумму. (срез)
            result += sum(digit_string)
            return f'Сумма равна: {result}'
        digit_string = list(map(int, string))  # делаю список чисел, чтобы искать сумму.
        result += sum(digit_string)
    return f'Сумма равна: {result}'

print(getsum())
