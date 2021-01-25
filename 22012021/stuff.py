from game import *


class Game:
    @staticmethod
    def play():
        card = CardGenerator.generate_card()
        from random import randint
        cnt_barrel = 90
        used_barrels = []
        while digit_in_card(card) is True:
            barrel = str(randint(1, 91))
            if barrel not in used_barrels:
                cnt_barrel -= 1
                print(f'Выпало число {barrel}. Осталось {cnt_barrel} бачонков')
                print(card, end='\n')
                used_barrels.append(barrel)
                answer = input('Вы хотите зачеркнуть число? Y (да)/ N(нет)')
                if any([answer == 'Y' and check_card(barrel, card),
                        answer == 'N' and check_card(barrel, card) == False]):  # проверка правильности действий игрока
                    if len(barrel) == 1:  # проверка если выпало однозначное число
                        card = card.replace(' ' + barrel + ' ',
                                            ' - ')  # чтобы не заменяло цифры в двухзначных числах, если выпало однозначное число
                    else:
                        card = card.replace(barrel, '-')  # просто заменяем число, если оно двухзначное
                else:
                    print('Вы проиграли')
                    break
        if digit_in_card(card) is False:
            print('Вы выиграли')


class CardGenerator:
    @staticmethod
    def generate_card():
        from random import randint
        s = set()
        card = '------ Ваша карточка -----\n** **          **    ** **\n   ** **     **   **    **\n** **    **    **    **\n--------------------------'
        while len(s) < 15:
            number = str(randint(1, 91))
            if number not in s:
                s.add(number)
                if len(number) == 1:
                    card = card.replace('**', ' ' + number, 1)
                else:
                    card = card.replace('**', number, 1)
            else:
                continue
        return card


game = Game()
game.play()
