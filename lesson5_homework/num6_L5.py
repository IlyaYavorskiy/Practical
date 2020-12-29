import re

final_dict = {}
subj_sum = 0

with open('num6_file_L5.txt', 'r', encoding='utf-8') as file:
    for i in file:
        cmd = i.split()
        for n in cmd:
            test = re.findall('\d+', n)
            if not test:
                continue
            else:
                subj_sum += int(test[0])
        final_dict[cmd[0][:-1]] = subj_sum
        subj_sum = 0
    print(final_dict)
