class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        from time import sleep
        sleep_time = [(7, 0), (2, 1), (4, 2)]
        for sec, color in sleep_time:   #Можно без цикла теоритически, но тогда нарушается принцип DRY
            print(TrafficLight.__color[color])
            sleep(sec)
        print('Конец цикла светофора')


lightme = TrafficLight()
lightme.running()


# Версия с проверкой правильности режима работы светофора

class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']  # эталонный порядок цветов

    def running(self):
        from time import sleep
        from random import choice
        sleep_time = [7, 2, 4]
        current_lights = []
        for sec in sleep_time:
            random_light = choice(TrafficLight.__color)  # светофор выдаёт цвета случайным образом
            print(random_light)
            sleep(sec)
            current_lights.append(random_light)  # добавляю текущий порядок цветов, чтобы сравнить с эталонным
        if TrafficLight.__color != current_lights:
            print('Светофор работает некорректно')
        else:
            print('Конец цикла светофора')


lightme = TrafficLight()
lightme.running()
