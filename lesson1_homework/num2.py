secondsFromUser = int(input('enter time in seconds '))
hours = secondsFromUser // 3600
secondsFromUser = secondsFromUser % 3600
minutes = secondsFromUser // 60
seconds = secondsFromUser % 60
print(f'{hours:02d} : {minutes:02d} : {seconds:02d}')
