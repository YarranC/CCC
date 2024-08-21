# A Knightly Pursuit
    
n = int(input())

for _ in range(n):
    r = int(input())
    c = int(input())

    pr = int(input())
    pc = int(input())

    kr = int(input())
    kc = int(input())

    kgrid = [[10000 for i in range(c+1)] for j in range(r+1)]
    kgrid[kr][kc] = 0

    old = [[kr, kc]]
    new = []
    
    while len(old) > 0:

        new = []
        for s in old:
            x, y = s
            v = kgrid[x][y] + 1

            if x - 2 > 0 and y + 1 <= c and kgrid[x - 2][y + 1] > v:
                kgrid[x - 2][y + 1] = v
                new.append([x - 2, y + 1])

            if x - 1 > 0 and y + 2 <= c and kgrid[x - 1][y + 2] > v:
                kgrid[x - 1][y + 2] = v
                new.append([x - 1, y + 2])

            if x + 1 <= r and y + 2 <= c and kgrid[x + 1][y + 2] > v:
                kgrid[x + 1][y + 2] = v
                new.append([x + 1, y + 2])

            if x + 2 <= r and y + 1 <= c and kgrid[x + 2][y + 1] > v:
                kgrid[x + 2][y + 1] = v
                new.append([x + 2, y + 1])

            if x + 2 <= r and y - 1 > 0 and kgrid[x + 2][y - 1] > v:
                kgrid[x + 2][y - 1] = v
                new.append([x + 2, y - 1])

            if x + 1 <= r and y - 2 > 0 and kgrid[x + 1][y - 2] > v:
                kgrid[x + 1][y - 2] = v
                new.append([x + 1, y - 2])

            if x - 1 > 0 and y - 2 > 0 and kgrid[x - 1][y - 2] > v:
                kgrid[x - 1][y - 2] = v
                new.append([x - 1, y - 2])

            if x - 2 > 0 and y - 1 > 0 and kgrid[x - 2][y - 1] > v:
                kgrid[x - 2][y - 1] = v
                new.append([x - 2, y - 1])
            
        old = new.copy()

    # check pawn position
    ppos = [pr, pc]
    pstep = 0

    while ppos[0] < r:
        x, y = ppos
        if kgrid[x][y] == pstep or kgrid[x][y] + 2 == pstep:
            print('Win in', pstep, 'knight move(s).')
            break
        if x + 1 <= r and kgrid[x+1][y] == pstep:
            print('Stalemate in', pstep, 'knight move(s).')
            break
        pstep+=1
        ppos[0]+=1

    if ppos[0] == r:
        print('Loss in', pstep - 1, 'knight move(s).')
    
