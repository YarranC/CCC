# Time on task
T = int(input())
C = int(input())

chores = []
for c in range(C):
    c = int(input())
    chores.append(c)

chores = sorted(chores)

time = chores[0]
cnt = 0
while time <= T:
    cnt+=1
    if cnt < C:
        time+=chores[cnt]
    else:
        break

print(cnt)
