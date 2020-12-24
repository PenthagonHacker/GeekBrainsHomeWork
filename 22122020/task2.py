lst, new_lst = [], []
while True:
    try:
        x = int(input('Введите число. По окончанию ввода чисел нажмите CTRL+D: '))
        lst.append(x)
    except EOFError:
        break
i = 1
while i < len(lst):
    new_lst.append(lst[i])
    new_lst.append(lst[i - 1])
    i += 2
if len(lst) % 2 != 0:
    new_lst.append(lst[-1])

print(new_lst)
