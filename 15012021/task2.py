class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, mass_per_sqm, depth):
        '''mass_per_sqm - масса(кг) асфальта для покрытия одного кв. метра дороги асфальтом.
        depth - толщина полотна(см)'''
        self.mass_per_sqm = mass_per_sqm
        self.depth = depth
        return f'{self._length * self._width * self.mass_per_sqm * self.depth / 1000:.0f} тонн'


road = Road(2000, 6)
mass = road.mass_calculation(25, 4)
print(mass)
