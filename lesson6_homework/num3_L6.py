class Worker:
    name = None
    surname = None
    position = None
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(int(self._income.get('wage')) + int(self._income.get('bonus')))


pos1 = Position('ivan', 'ivanov', 'manager', 55555, 22222)
pos1.get_full_name()
pos1.get_total_income()
print(pos1.name)
print(pos1.surname)

pos2 = Position('petr', 'petrov', 'driver', 44444, 11111)
pos2.get_full_name()
pos2.get_total_income()
print(pos2.name)
print(pos2.surname)