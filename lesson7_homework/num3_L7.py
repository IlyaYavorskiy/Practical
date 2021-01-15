class Cell:
    def __init__(self, count):
        self.count = count
        print(f'{self.count} cells in a cell')

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        if (self.count - other.count) > 0:
            return self.count - other.count
        else:
            print('negative cell difference')
            return 0

    def __mul__(self, other):
        return self.count * other.count

    def __floordiv__(self, other):
        return self.count // other.count

    def make_order(self, line):
        return '\n'.join(['*' * line for _ in range(self.count // line)]) + '\n' + '*' * (self.count % line)


q = Cell(7)
w = Cell(5)
e = Cell(q + w)
r = Cell(q - w)
t = Cell(q * w)
y = Cell(q // w)
print(q.make_order(3))
