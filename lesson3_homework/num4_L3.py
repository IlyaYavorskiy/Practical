def my_func(x, y):
    power = 1
    for i in range(abs(y)):
        power *= x
        i += 1
    return power


x = float(input('введите действительное положительное число x '))
y = int(input('введите целое отрицательное число y '))
if y >= 0 or x <= 0:
    print('проверьте значение числе x и y')
else:
    print(f'the value of x to the power of y is : {my_func(x, y)}')
