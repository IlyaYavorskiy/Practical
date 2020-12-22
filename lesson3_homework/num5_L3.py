sum = 0
exit = 0
while exit != True:
    list = input('enter numbers separated by spaces. to exit press "q" ').split()
    for i in list:
        try:
            if i == 'q':
                print('EXIT')
                exit = 1
                break
            else:
                sum += int(i)
        except ValueError:
            print('to exit press "q"')
            continue
    print(f'sum = {sum}')
