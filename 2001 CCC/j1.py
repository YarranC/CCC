# Dressing Up

H = int(input())

for i in range(H):
    if i < H//2:
        c = 2*i+1
        for _ in range(c):
            print('*', sep='', end='')
        for _ in range(2*H-2*c):
            print(' ', sep='', end='')
        for _ in range(c):
            print('*', sep='', end='')

    elif i == H//2:
        for _ in range(2*H):
           print('*', sep='', end='')
 
    else:
        c = 2*H - 2*i - 1
        for _ in range(c):
            print('*', sep='', end='')
        for _ in range(2*H-2*c):
            print(' ', sep='', end='')
        for _ in range(c):
            print('*', sep='', end='')
    print()   
