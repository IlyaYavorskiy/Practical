firstDayDistance = int(input('enter your progress '))
maxDistance = int(input('enter your desired result '))
day = 1
while firstDayDistance <= maxDistance:
    day += 1
    firstDayDistance *= 1.1
    print(f'{day} day: {firstDayDistance:.2f} kilometers')
print(f'Answer: at day {day} sportsman achieve the result - at least {maxDistance} kilometers')
