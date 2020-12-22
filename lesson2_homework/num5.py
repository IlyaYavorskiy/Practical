my_list = [7, 5, 3, 3, 2]
new_element = int(input('enter new element '))
for i in range(len(my_list)):
    if new_element > my_list[i]:
        my_list.insert(i, new_element)
        break
    elif new_element <= my_list[-1]:
        my_list.append(new_element)
        break
print(my_list)

# my_list.insert(0, new_element) if new_element > my_list[0] else my_list.insert(-my_list[::-1].index(new_element), new_element) if new_element in my_list else my_list.append(new_element)
