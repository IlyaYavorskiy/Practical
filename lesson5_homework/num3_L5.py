with open('num3_file_L5.txt', 'r', encoding='utf-8') as file:
    average_salary = 0
    names_salary = file.readlines()
    print('names whose salaries are less than 20 thousand:')
    for i in names_salary:
        average_salary += int(i.split()[1])
        if int(i.split()[1]) < 20000:
            print(i.split()[0])
        else:
            continue
    print(f'average salary = {average_salary / len(names_salary)}')
