with open('num2_file_L5.txt', 'r', encoding='utf-8') as file:
    txt = file.readlines()
    print(f'{len(txt)} lines in the file')
    count = 1
    for i in txt:
        i.split()
        print(f'line number {count} contains {len(i.split())} words')
        count += 1
