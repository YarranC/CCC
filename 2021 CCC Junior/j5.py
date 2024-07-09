# Modern Art

M = int(input())
N = int(input())


r = [0 for _ in range(M)]
c = [0 for _ in range(N)]

for _ in range(int(input())):
    d, n = input().split()
    n = int(n) - 1

    if d == 'R':
        r[n]+=1
    else:
        c[n]+=1

cnt = 0
for i in range(M):
    for j in range(N):
        if (r[i]+c[j])%2 == 1:
            cnt+=1

print(cnt)
