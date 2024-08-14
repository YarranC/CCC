# Mountain passage

trip = int(input())

for t in range(trip):
    n = int(input())
    
    grid = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dist = [[999 for _ in range(n+1)] for _ in range(n+1)]
    for x in range(1, n+1):
        for y in range(1, n+1):
            grid[x][y] = int(input())

    old = [[1,1]]
    new = []
            
    ox = grid[1][1]
    dist[1][1] = 0

    while len(old) > 0:
        #input()
        #print(old)
        new = []
        for j in range(len(old)):
            x, y = old[j]
            if x - 1 > 0 and dist[x-1][y] > dist[x][y] and \
               abs(grid[x-1][y] - grid[x][y]) <= 2:
                temp = dist[x-1][y]
                if grid[x-1][y] > ox or grid[x][y] > ox:
                    dist[x-1][y] = dist[x][y] + 1
                else:
                    dist[x-1][y] = dist[x][y]
                if dist[x-1][y] < temp:
                    new.append([x-1,y])
            if x + 1 < n+1 and dist[x+1][y] > dist[x][y] and \
               abs(grid[x+1][y] - grid[x][y]) <= 2:
                temp = dist[x+1][y]
                if grid[x+1][y] > ox or grid[x][y] > ox:
                    dist[x+1][y] = dist[x][y] + 1
                else:
                    dist[x+1][y] = dist[x][y]
                if dist[x+1][y] < temp:
                    new.append([x+1,y])
            if y - 1 > 0 and dist[x][y-1] > dist[x][y] and \
               abs(grid[x][y-1] - grid[x][y]) <= 2:
                temp = dist[x][y-1]
                if grid[x][y-1] > ox or grid[x][y] > ox:
                    dist[x][y-1] = dist[x][y] + 1
                else:
                    dist[x][y-1] = dist[x][y]
                if dist[x][y-1] < temp:
                    new.append([x,y-1])
            if y + 1 < n+1 and dist[x][y+1] > dist[x][y] and \
               abs(grid[x][y+1] - grid[x][y]) <= 2:
                temp = dist[x][y+1]
                if grid[x][y+1] > ox or grid[x][y] > ox:
                    dist[x][y+1] = dist[x][y] + 1
                else:
                    dist[x][y+1] = dist[x][y]
                if dist[x][y+1] < temp:
                    new.append([x,y+1])
        old = new.copy()

    if dist[n][n] == 999:
        print('CANNOT MAKE TRIP')
    else:
        print(dist[n][n])

    if t < trip - 1:
        print()
