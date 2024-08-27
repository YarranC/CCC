# Spirals (Exact Version)

num = int(input())
for idx in range(num):
    x, y = [int(i) for i in input().split()]

    if x == y:
        print(x)
    else:
        n = int(pow(y - x + 1, 0.5))
        if pow(n, 2) != (y - x + 1):
            n += 1

        grid = [[' ' for _ in range(n)] for _ in range(n)]

        a = b = (n-1)//2
        d = 'l'
        for i in range(x, y+1):
            grid[a][b] = str(i)
            match d:
                case 'd':
                    if a + 1 < n and grid[a][b+1] != ' ':
                        a = a + 1
                    else:
                        b = b + 1
                        d = 'r'
                case 'r':
                    if b + 1 < n and grid[a-1][b] != ' ':
                        b = b + 1
                    else:
                        a = a - 1
                        d = 'u'
                case 'u':
                    if a - 1 >= 0 and grid[a][b-1] != ' ':
                        a = a - 1
                    else:
                        b = b - 1
                        d = 'l'
                case 'l':
                    if b - 1 >= 0 and grid[a+1][b] != ' ':
                        b = b - 1
                    else:
                        a = a + 1
                        d = 'd'

        left = False
        right = False

        for i in range(n):
            if grid[i][0] != ' ':
                left = True
            if grid[i][n-1] != ' ':
                right = True
                
        width = [0 for _ in range(n)]
        for j in range(n):
            l = 0
            for i in range(n):
                if len(grid[i][j]) > l:
                    l = len(grid[i][j])
            width[j] = l
           
        for i in range(n):
            for j in range(n):
                if (j == 0 and left == True) or (j != 0 and j != n - 1) or (j == n - 1 and right == True):
                    for _ in range(width[j] - len(grid[i][j])):
                        print(' ', end='')
                    print(grid[i][j], end='')
                    if n > 2 and (j < n - 2 or (j == n - 2 and right == True)):
                        print(' ', end='')
                    elif n == 2 and j < n - 1 and right == True:
                        print(' ', end='')
            print()

    if idx < num - 1:
        print()
