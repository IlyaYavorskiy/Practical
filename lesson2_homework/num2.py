stringFromUser = input('enter list items separated by space ').split()
for i in range(0, len(stringFromUser) - 1, 2):
    stringFromUser[i], stringFromUser[i + 1] = stringFromUser[i + 1], stringFromUser[i]
print(stringFromUser)
