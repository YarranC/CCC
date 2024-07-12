# Tandem Bicycle

Q = int(input())
N = int(input())
D = input().split()
P = input().split()

for i in range(N):
    D[i] = int(D[i])
    P[i] = int(P[i])

D.sort()
P.sort()
    
s = None
for _ in range(N):
    t = 0
    for i in range(N):
        t += max(int(D[i]), int(P[i]))
    if s == None:
        s = t
    elif Q == 2 and t > s:
        s = t
    elif Q == 1 and t < s:
        s = t
    a = P.pop(0)
    P.append(a)

print(s)
