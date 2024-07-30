# Problem J5/S3 - Floor Plan

floor = int(input())

row = int(input())
col = int(input())

grid = [['' for _ in range(col)] for _ in range(row)]

for r in range(row):
    i = input()
    for c in range(col):
        grid[r][c] = i[c]

sizes = []

def check(x, y):
    s = 0

    if x >= 0 and x < row and y >= 0 and y < col and grid[x][y] == '.':
        grid[x][y] = '*'
        s = 1 + check(x+1, y) + check(x-1, y) + check(x, y-1) + check(x, y+1)
    return s

for r in range(row):
    for c in range(col):
        s = check(r, c)
        if s != 0:
            sizes.append(s)

sizes.sort(reverse=True)
rooms = 0
for s in sizes:
    if floor - s >= 0:
        rooms+=1
        floor-=s
    else:
        break

if rooms == 1:
    print(rooms, 'room,', floor, 'square metre(s) left over')
else:
    print(rooms, 'rooms,', floor, 'square metre(s) left over')
