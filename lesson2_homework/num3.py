month = int(input('enter your month 1 - 12 '))

list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn',
        'winter']
for ind, el in enumerate(list, 1):
    if month == ind:
        print(el)

# list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
# if month in list[0]:
#     print('winter')
# elif month in list[1]:
#     print('spring')
# elif month in list[2]:
#     print('summer')
# elif month in list[3]:
#     print('autumn')
# else:
#     print('incorrect month')

dict = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [5, 6, 7], 'autumn': [9, 10, 11]}
for i in dict:
    if month in dict[i]:
        print(i)
