# CCC Othello

grid = [[0 for _ in range(8)] for _ in range(8)]

line = input().split()

cfg = line[0]
match cfg:
    case 'a':
        grid[3][3] = 'w'
        grid[3][4] = 'b'
        grid[4][3] = 'b'
        grid[4][4] = 'w'
    case 'b':
        for i in range(8):
            grid[i][i] = 'b'
            grid[i][8-i-1] = 'w'
    case 'c':
        for i in range(8):
            grid[i][2] = 'b'
            grid[i][3] = 'b'
            grid[i][4] = 'w'
            grid[i][5] = 'w'

step = int(line[1])
line = line[2:]

for i in range(step):
    if i%2 == 0:
        s = 'b'
    else:
        s = 'w'

    r = int(line[i*2]) - 1
    c = int(line[i*2+1]) - 1
    grid[r][c] = s

    # left
    e = c
    f = False
    while e >= 0:
        e-=1
        if e >= 0 and grid[r][e] == 0:
            break
        elif e >= 0 and grid[r][e] == s:
            f = True
            break

    if f:
        for i in range(e, c):
            grid[r][i] = s

    # right
    e = c
    f = False
    while e < 8:
        e+=1
        if e < 8 and grid[r][e] == 0:
            break
        elif e < 8 and grid[r][e] == s:
            f = True
            break
        
    if f:
        for i in range(c, e):
            grid[r][i] = s

    # up
    e = r
    f = False
    while e >= 0:
        e-=1
        if e >= 0 and grid[e][c] == 0:
            break
        elif e >=0 and grid[e][c] == s:
            f = True
            break

    if f:
        for i in range(e, r):
            grid[i][c] = s

    # down
    e = r
    f = False
    while e < 8:
        e+=1
        if e < 8 and grid[e][c] == 0:
            break
        elif e < 8 and grid[e][c] == s:
            f = True
            break

    if f:
        for i in range(r, e):
            grid[i][c] = s

    # top left
    e = c
    d = r
    f = False
    while e >= 0 and d >= 0:
        e-=1
        d-=1
        if e >= 0 and d >= 0 and grid[d][e] == 0:
            break
        elif e >= 0 and d >= 0 and grid[d][e] == s:
            f = True
            break

    if f:
        for i in range(e, c):
            grid[d][i] = s
            d+=1

    # top right
    e = c
    d = r
    f = False
    while e < 8 and d >= 0:
        e+=1
        d-=1
        if e < 8 and d >= 0 and grid[d][e] == 0:
            break
        elif e < 8 and d >= 0 and grid[d][e] == s:
            f = True
            break

    if f:
        d = r
        for i in range(c, e):
            grid[d][i] = s
            d-=1

    # bottom left
    e = c
    d = r
    f = False
    while e >= 0 and d < 8:
        e-=1
        d+=1
        if e >= 0 and d < 8 and grid[d][e] == 0:
            break
        elif e >= 0 and d < 8 and grid[d][e] == s:
            f = True
            break

    if f:
        for i in range(e, c):
            grid[d][i] = s
            d-=1

    # bottom right
    e = c
    d = r
    f = False
    while e < 8 and d < 8:
        e+=1
        d+=1
        if e < 8 and d < 8 and grid[d][e] == 0:
            break
        elif e < 8 and d < 8 and grid[d][e] == s:
            f = True
            break

    if f:
        d = r
        for i in range(c, e):
            grid[d][i] = s
            d+=1
    
white = 0
black = 0
for i in range(8):
    for j in range(8):
        if grid[i][j] == 'w':
            white+=1
        elif grid[i][j] == 'b':
            black+=1

print(black, white)
