def int_func(text):
    return text.title()


string_from_user = input('enter your words in Latin and in lower case ').split()
for i in string_from_user:
    if i.islower() and u'\u0061' <= i <= u'\u007A':
        print(int_func(i))
    else:
        continue
