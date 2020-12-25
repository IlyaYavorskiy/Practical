def division(a, b):
    return a / b


try:
    print(division(int(input('enter firs number ')), int(input('enter second number '))))
except (ZeroDivisionError, ValueError):
    print('please enter a number and remember that division by 0 is not allowed')
