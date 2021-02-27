class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


number1 = input('Введите число 1: ')
number2 = input('Введите число 2: ')

try:
    number1 = int(number1)
    number2 = int(number2)
    if number2 == 0:
        raise OwnError('Вы ввели второе значение 0. Программа будет завершена')
    res = number1 / number2
except ValueError:
    print('Вы ввели не число(а). Программа будет завершена')
except OwnError as zero_error:
    print(zero_error)
else:
    print(f'Результат: {res}')
