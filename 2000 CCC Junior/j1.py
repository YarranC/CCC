# Calendar

weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat']
start_day, num_days = [int(i) for i in input().split()]

print(*weekdays, sep=' ', end='\n')

day = 2-start_day
string = []
while day < num_days:
    if day <= 0:
        string.append('   ')
    elif day < 10:
        string.append('  ')
        string.append(day)
    else:
        string.append(' ')
        string.append(day)
    day+=1
    if (day+start_day-2)%7 == 0:
        print(*string, sep='', end='\n')
        string = []
    else:
        string.append(' ')
string.append(' '+str(day))
if string != []:
    print(*string, sep='', end='\n')
