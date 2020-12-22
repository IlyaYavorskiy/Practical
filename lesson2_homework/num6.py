products = []
tmp = 1

name_list = []
price_list = []
quantity_list = []
unit_list = []
analytics = {}

while True:
    answer = input('Would you like to add a product? (yes/no) ')
    if answer == 'yes':
        name = input('please enter product name ')
        price = int(input('please enter product price '))
        quantity = int(input('please enter product quantity '))
        unit = input('please enter product unit ')
        products.append((tmp, {'name': name, 'price': price, 'quantity': quantity, 'unit': unit}))
        tmp += 1
        print(products)
    elif answer == 'no':
        for i in range(len(products)):
            name_list.append(products[i][1]['name'])
            price_list.append(products[i][1]['price'])
            quantity_list.append(products[i][1]['quantity'])
            unit_list.append(products[i][1]['unit'])
        analytics = {'name': name_list, 'price': price_list, 'quantity': quantity_list, 'unit': unit_list}
        print('Analytics composes: ' + str(analytics))
        break
    else:
        print('please enter (yes/no)')
