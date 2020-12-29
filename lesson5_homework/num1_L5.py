with open('num1_file_L5.txt', 'w', encoding='utf-8') as file:
    while True:
        string_from_user = input('enter your string ')
        file.write(f'{string_from_user}\n')
        if string_from_user == "":
            break
