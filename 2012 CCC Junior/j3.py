# Icon Scaling

icon = [['*', 'x', '*'],[' ', 'x', 'x'],['*', ' ', '*']]

k = int(input())

for i in range(3):
    s = ''
    for j in range(3):
        for _ in range(k):
            s+=icon[i][j]
    for _ in range(k):
        print(s)
