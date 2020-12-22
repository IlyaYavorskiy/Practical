fromUser = input('enter list items separated by space ').split()
for ind, el in enumerate(fromUser, 1):
    print(ind, el) if len(el) <= 10 else print(ind, el[:10])
