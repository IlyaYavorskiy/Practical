def my_func(a, b, c):
    my_list = [a, b, c]
    min_num = min(my_list)
    my_list.remove(min_num)
    print(my_list[0] + my_list[1])


my_func(int(input('enter a ')), int(input('enter b ')), int(input('enter c ')))
