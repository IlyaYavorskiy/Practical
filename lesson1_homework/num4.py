numberFromUser = int(input('enter your number '))
maxNumber = 0
while numberFromUser != 0:
    lastNumber = numberFromUser % 10
    if lastNumber > maxNumber:
        maxNumber = lastNumber
    numberFromUser //= 10
print(f'max number = {maxNumber}')
