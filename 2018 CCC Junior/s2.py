# Sunflowers

N = int(input())
F = []
for i in range(N):
    F.append(input().split())

a = int(F[0][0])
b = int(F[0][1])
c = int(F[1][0])

# original direction
if a < b and a < c:
    for i in range(N):
        q = F[i]
        print(*q, sep = ' ')

# turned 180 degrees       
if a > b and a > c:
    for i in range(N):
        q = []
        for j in range(N):
            q.append(F[N-i-1][N-j-1])
        print(*q, sep = ' ')

# conterclock wise 90 degrees
if a < b and a > c:
    for i in range(N):
        q = []        
        for j in range(N):
            q.append(F[N-j-1][i])
        print(*q, sep = ' ')

#clock wise 90 degrees
if a > b and a < c:
    for i in range(N):
        q = []
        for j in range(N):
            q.append(F[j][N-i-1])
        print(*q, sep = ' ')    
