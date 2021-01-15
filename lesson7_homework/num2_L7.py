from abc import ABC, abstractmethod


class Clothes(ABC):
    total_result = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    @property
    def expense(self):
        result = self.size / 6.5 + 0.5
        Clothes.total_result += result
        return f'fabric consumption for a {self.color} coat = {result:.2f}'


class Suit(Clothes):
    def __init__(self, color, height):
        self.color = color
        self.height = height

    @property
    def expense(self):
        result = self.height * 2 + 0.3
        Clothes.total_result += result
        return f'fabric consumption for a {self.color} suit = {result:.2f}'


coat = Coat('black', 400)
print(coat.expense)
suit = Suit('white', 500)
print(suit.expense)

print(f'total fabric consumption for a Clothes = {Clothes.total_result:.2f}')