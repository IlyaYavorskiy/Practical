# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name, hours, per_hour, prize = argv


def form(hours, per_hour, prize):
    return (int(hours) * float(per_hour)) + int(prize)


try:
    print(f'salary = {form(argv[1], argv[2], argv[3])} $')
except ValueError:
    print('please enter hours(int), per_hour(float), prize(int)')
