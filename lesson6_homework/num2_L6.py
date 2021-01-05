class Road:
    _length = None
    _width = None
    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self.le = length
        self.wi = width

    def my_func(self):
        return (self.le * self.wi * self.weight * self.thickness) / 1000


r1 = Road(20, 5000)
print(f'{int(r1.my_func())} тонн.')
