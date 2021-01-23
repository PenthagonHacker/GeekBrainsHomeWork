class CardGenerator:
    pass


# проверка есть ли число в карточке
def check_card(barrel):
    with open('player.txt') as player:
        file = player.read()
        if str(barrel) in file:
            return True
        else:
            return False


# метод игра#
with open('player.txt', 'r+', encoding='utf-8') as card:
    from random import randint

    used_barrels = []
    while len(used_barrels) < 15:
        #todo Нам необходимо написать условие выхода из цикла для случая если игрок или комп закрыли все числа в карточке.
        #todo Я не могу врубиться как оъяснить программе, что все числа в карточке закончились =\
        card.seek(0)  # 'каретку' в начало файла  иначе не работает !!!!!
        file = card.read() # читаем содержимое файла
        barrel = str(randint(1, 91))
        if barrel not in used_barrels:
            print(f'Выпало число {barrel}')
            print(file, end='\n')
            used_barrels.append(barrel)
            answer = input('Вы хотите зачеркнуть число? Y (да)/ N(нет)')
            if any([answer == 'Y' and check_card(barrel), answer == 'N' and check_card(barrel) == False]): # проверка правильности действий игрока
                if len(barrel) == 1:  # проверка если выпало однозначное число
                    file = file.replace(' ' + barrel + ' ', ' - ')  # чтобы не заменяло цифры в двухзначных числах, если выпало однозначное число
                else:
                    file = file.replace(barrel, '-')  # просто заменяем число, если оно двухзначное
                card.seek(0)  # здесь тоже 'каретку' в начало файла иначе не работает !!!!
                card.write(file)
            else:
                print('Вы проиграли')
                break
