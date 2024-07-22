# What is n, Daddy?

n = int(input())

cnt = 0
for l in range(6):
    for r in range(0, l+1):
        if l+r == n:
            cnt+=1

print(cnt)
