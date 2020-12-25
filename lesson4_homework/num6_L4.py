# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# lastОбратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle

start_num = int(input('please enter the initial value '))
last_num = int(input('enter the end value '))
for i in count(start_num):
    if i > last_num:
        break
    else:
        print(i)

list_from_user = input('please enter your string ')
counter = int(input('enter the number of times '))
tmp = 0
for n in cycle(list_from_user):
    if tmp > counter:
        break
    print(n)
    tmp += 1
