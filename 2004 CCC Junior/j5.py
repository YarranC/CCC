# Problem J5: Fractals

level, width, x = [eval(i) for i in input().split()]

grid = [[0 for _ in range(int((width+1)/2))] for _ in range(width+1)]

for i in range(width+1):
    grid[i][0] = 1

memo = [[(0, 0), (width,0), 'u']]
temp = []

def update(start, end, direction):
    global temp

    temp.append([start, end, direction])

    match direction:
        case 'u':
            x1 = start[0]
            x2 = end[0]
            y = start[1]
            for x in range(x1, x2+1):
                grid[x][y] = 1
        case 'd':
            x1 = start[0]
            x2 = end[0]
            y = start[1]
            for x in range(x2, x1+1):
                grid[x][y] = 1
        case 'l':
            x = start[0]
            y1 = start[1]
            y2 = end[1]
            for y in range(y1, y2+1):
                grid[x][y] = 1
        case 'r':
            x = start[0]
            y1 = start[1]
            y2 = end[1]
            for y in range(y2, y1+1):
                grid[x][y] = 1

def fractal(m):
    global memo, grid, width
    
    start, end, direction = m
    match direction:
        case 'u':
            f = int(abs(end[0] - start[0])/3)
            for x in range(start[0], end[0]+1):
                grid[x][start[1]] = 0
            update(start, (start[0]+f, start[1]), 'u')
            update((start[0]+f, start[1]), (start[0]+f, start[1]+f), 'l')
            update((start[0]+f, start[1]+f), (start[0]+2*f, start[1]+f), 'u')
            update((start[0]+2*f, start[1]+f), (start[0]+2*f, start[1]), 'r')
            update((start[0]+2*f, start[1]), end, 'u')
        case 'l':
            f = int(abs(end[1] - start[1])/3)
            for y in range(start[1], end[1]+1):
                grid[start[0]][y] = 0
            update(start, (start[0], start[1]+f), 'l')
            update((start[0], start[1]+f), (start[0]-f, start[1]+f), 'd')
            update((start[0]-f, start[1]+f), (start[0]-f, start[1]+2*f), 'l')
            update((start[0]-f, start[1]+2*f), (start[0], start[1]+2*f), 'u')
            update((start[0], start[1]+2*f), end, 'l')
        case 'd':
            f = int(abs(end[0] - start[0])/3)
            for x in range(end[0], start[0]+1):
                grid[x][start[1]] = 0
            update(start, (start[0]-f, start[1]), 'd')
            update((start[0]-f, start[1]), (start[0]-f, start[1]-f), 'r')
            update((start[0]-f, start[1]-f), (start[0]-2*f, start[1]-f), 'd')
            update((start[0]-2*f, start[1]-f), (start[0]-2*f, start[1]), 'l')
            update((start[0]-2*f, start[1]), end, 'd')
        case 'r':
            f = int(abs(end[1] - start[1])/3)
            for y in range(end[1], start[1]+1):
                grid[start[0]][y] = 0
            update(start, (start[0], start[1]-f), 'r')
            update((start[0], start[1]-f), (start[0]+f, start[1]-f), 'u')
            update((start[0]+f, start[1]-f), (start[0]+f, start[1]-2*f), 'r')
            update((start[0]+f, start[1]-2*f), (start[0], start[1]-2*f), 'd')
            update((start[0], start[1]-2*f), end, 'r')

     
for i in range(1, level+1):
    for m in memo:
        fractal(m)

    memo = temp
    temp = []
        
for i in range(int((width+1)/2)):
    if grid[x][i] == 1:
        print(i+1, end=' ')
