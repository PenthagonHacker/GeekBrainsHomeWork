class Storage:
    pass


class OfficeEquipment:
    def __init__(self, model, price, made_in):
        self.model = model  # модель
        self.price = price  # цена
        self.made_in = made_in  # страна производитель


class Printer(OfficeEquipment):
    def __init__(self, model, price, made_in, blacknwhite=True):
        super().__init__(model, price, made_in)
        self.blacknwhite = blacknwhite  # чёрнобелый или нет


class Scaner(OfficeEquipment):
    def __init__(self, model, price, made_in, quality):
        super().__init__(model, price, made_in)
        self.quality = quality  # качество печати


class Xerox(OfficeEquipment):
    def __init__(self, model, price, made_in, copy_speed):
        super().__init__(model, price, made_in)
        self.copy_speed = copy_speed  # скорость печати