from functools import reduce

with open('num5_file_L5', 'w', encoding='utf-8') as file:
    file.write(input('enter numbers separated by a space '))

summa = 0

with open('num5_file_L5', 'r', encoding='utf-8') as file:
    list_strings = file.read().split()
    list_nums = [int(i) for i in list_strings]


def my_func(a, b):
    return a + b


print(f'sum of numbers in file = {reduce(my_func, list_nums)}')
