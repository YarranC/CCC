# Happy or Sad

happy = 0
sad = 0

cur = ''
for c in input():
    if c == ':':
        cur = c
    elif c == '-' and cur == ':':
        cur = '-'
    elif c == ')' and cur == '-':
        happy += 1
        cur = ''
    elif c == '(' and cur == '-':
        sad += 1
        cur = ''

if happy == 0 and sad == 0:
    print('none')
elif happy  == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')
