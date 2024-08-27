# Spirals

x = int(input())
y = int(input())

if x == y:
    print(x)
    import sys
    sys.exit(0)

n = int(pow(y - x + 1, 0.5))
if pow(n, 2) != (y - x + 1):
    n += 1

grid = [[' ' for _ in range(n)] for _ in range(n)]

a = b = (n-1)//2
d = 'l'
for i in range(x, y+1):
    grid[a][b] = i
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

for i in range(n):
    print(*grid[i])
                
            
