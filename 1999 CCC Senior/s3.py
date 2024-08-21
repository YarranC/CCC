# Divided Fractals

grid = []

def factal(n, x, y):
    global grid
    
    if n == 1:
        grid[x+1][y+1] = ' '
    else:
        w = pow(3, n-1)
        f = w
        s = 2 * w

        for i in range(f, s):
            for j in range(f, s):
                grid[x+i][y+j] = ' '
    
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    factal(n-1, x + i*pow(3, n-1), y + j*pow(3, n-1))
    
for _ in range(int(input())):

    n = int(input())
    b = int(input())
    t = int(input())
    l = int(input())
    r = int(input())
    
    if n == 0:
        print('*')      
    else:
        w = pow(3, n)
        grid = [['*' for _ in range(w)] for _ in range(w)]

        factal(n, 0, 0)
        
        for i in range(w-t, w-b+1):
            for j in range(l-1, r):
                if j < r-1:
                    print(grid[i][j], end=' ')
                else:
                    print(grid[i][j])
    print()

            
        
