# S3J5 - Blindfold

row = int(input())
col = int(input())

grid = [['.' for _ in range(col)] for _ in range(row)]
pos = []

for r in range(row):
    line = input()
    for c in range(col):
        grid[r][c] = line[c]
        if line[c] != 'X':
            pos.append([r,c,'n'])
            pos.append([r,c,'s'])
            pos.append([r,c,'w'])
            pos.append([r,c,'e'])

ins = int(input())
    
for _ in range(ins):
    i = input()
    match i:
        case 'F':
            new = []
            for p in pos:
                match p[2]:
                    case 'n':
                        if p[0]-1 >= 0 and grid[p[0]-1][p[1]] != 'X':
                            new.append([p[0]-1, p[1], 'n'])
                    case 's':
                        if p[0]+1 < row and grid[p[0]+1][p[1]] != 'X':
                            new.append([p[0]+1, p[1], 's'])
                    case 'w':
                        if p[1]-1 >= 0 and grid[p[0]][p[1]-1] != 'X':
                            new.append([p[0], p[1]-1, 'w'])
                    case 'e':
                        if p[1]+1 < col and grid[p[0]][p[1]+1] != 'X':
                            new.append([p[0], p[1]+1, 'e'])
            pos = new               
                    
        case 'L':
            for p in range(len(pos)):
                match pos[p][2]:
                    case 'n':
                        pos[p][2] = 'w'
                    case 's':
                        pos[p][2] = 'e'
                    case 'w':
                        pos[p][2] = 's'
                    case 'e':
                        pos[p][2] = 'n'
        case 'R':
            for p in range(len(pos)):
                match pos[p][2]:
                    case 'n':
                        pos[p][2] = 'e'
                    case 's':
                        pos[p][2] = 'w'
                    case 'w':
                        pos[p][2] = 'n'
                    case 'e':
                        pos[p][2] = 's'

for p in pos:
    grid[p[0]][p[1]] = '*'

for r in range(row):
    for c in range(col):
        print(grid[r][c], end='')
    print()
    
