class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('draw now')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} draw now')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} draw now')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} draw now')


pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()