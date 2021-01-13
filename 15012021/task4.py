class Car:
    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def speed_up(self, acceleration):   # просто решил добавить ускорение автомобиля, тренировался...
        self.speed += acceleration

    @staticmethod
    def go():
        return 'The car is moving now'

    def stop(self):
        self.speed = 0
        return 'The car has stoped'

    def show_speed(self):
        return 'The current speed is {speed} mphr'.format(speed=self.speed)

    def turn(self, direction):
        return 'The car has turned right' if direction == 'right' else 'The car has turned left'


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police=True):
        super().__init__(speed, color, name, is_police)

class TownCar(Car):
    def show_speed(self):
        return 'Overspeeding'if self.speed > 60 else 'The current speed is {speed} mphr'.format(speed=self.speed)

class WorkCar(Car):
    def show_speed(self):
        return 'Overspeeding' if self.speed > 40 else 'The current speed is {speed} mphr'.format(speed=self.speed)




car = SportCar(60, 'blue', 'mazeratti')
police = PoliceCar(60, 'red', 'chevelle')
town_car = TownCar(80, 'black', 'toyota')
work_car = WorkCar(30, 'white', 'zaporozhec')

car.speed_up(20)
car.speed_up(20)

print(car.show_speed())
print(car.turn('left'))
print(car.go())
print(car.stop())
print(car.show_speed())
print(car.is_police)
print(police.is_police)
print(town_car.show_speed())
print(work_car.is_police)
