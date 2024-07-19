# Unfriend

import sys

N = int(input())
if N == 1:
    print(1)
    sys.exit(0)
    
friends = dict()

for i in range(1, N):
    j = int(input())
    if friends.get(j) == None:
        friends[j] = [i]
    else:
        friends[j].append(i)
        
memo = {}

def unfriend(n):
    if n in memo:
        return memo[n]
    
    global friends
    if friends.get(n) == None:
        memo[n] = 1
        return 1
    
    num = len(friends[n])
    cnt = 1
    count = [0 for _ in range(num)]
    for i in range(num):
        count[i] = unfriend(friends[n][i])
        cnt += count[i]

    for i in range(num):
        for j in range(i+1, num):
            cnt += count[i]*count[j]
    if num >= 3:
        for i in range(num):
            for j in range(i+1, num):
                for k in range(j+1, num):
                    cnt += count[i]*count[j]*count[k]
                
    if num >= 4:
        for i in range(num):
            for j in range(i+1, num):
                for k in range(j+1, num):
                    for m in range(k+1, num):
                        cnt += count[i]*count[j]*count[k]*count[m]

    if num >= 5:
        for i in range(num):
            for j in range(i+1, num):
                for k in range(j+1, num):
                    for l in range(k+1, num):
                        for m in range(l+1, num):
                            cnt += count[i]*count[j]*count[k]*count[l]*count[m]
    memo[n] = cnt
    return cnt

print(unfriend(N))
