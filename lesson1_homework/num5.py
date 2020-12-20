income = int(input('enter your income '))
costs = int(input('enter your costs '))
pure = income - costs
if income < costs:
    print(f'income lower than costs by {pure}')
elif income > costs:
    print(f'your pure income equals {pure}')
    profitability = pure / income
    print(f'your profitability = {profitability:.2f}')
    incomePerEmployee = pure / int(input('enter number of employee '))
    print(f'income per employee = {incomePerEmployee:.2f}')
else:
    print('income equals costs')
