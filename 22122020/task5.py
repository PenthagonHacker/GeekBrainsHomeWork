my_list = [11, 11, 10, 9, 9, 7, 5, 4, 1, 1, 0]

num = int(input('Введите число: '))

my_list.append(num)
my_list = sorted(my_list, reverse=True)
print(my_list)
