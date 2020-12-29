translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('num4_file_L5.txt', 'r', encoding='utf-8') as file_read:
    for i in file_read:
        cmd = i.split()
        cmd[0] = translate.get(cmd[0])

        with open('num4.1_file_L5.txt', 'a', encoding='utf-8') as file_write:
            file_write.write(f"{' '.join(cmd)}\n")
