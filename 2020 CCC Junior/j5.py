# Escape Room

import sys
from collections import deque

M = int(input())
N = int(input())

room = [[] for _ in range(M*N + 1)]

for r in range(M):
    c = 1
    for num in map(int, input().split()):
        if num <= M*N:
            room[(r+1)*c].append(num)  
        c += 1

status = [False for _ in range(M*N + 1)]
status[1] = True
q = deque([1])

while q:
    cur = q.popleft()

    if cur == M*N:
        print("yes")
        sys.exit() 

    for i in room[cur]:
        if not status[i]:
            status[i] = True
            q.append(i)

print("no")
