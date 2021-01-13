class Stationery:
    title = ''

    @staticmethod
    def draw():
        return 'Запуск отрисовки'


class Pen(Stationery):
    title = 'Pen'

    @classmethod
    def draw(cls):
        return f'I draw with my {cls.title}'


class Pencil(Stationery):
    title = 'Pencil'

    @classmethod
    def draw(cls):
        return f'I draw with my {cls.title}'


class Handle(Stationery):
    title = 'Handle'

    @classmethod
    def draw(cls):
        return f'I draw with my {cls.title}'


stat = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

print(stat.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())