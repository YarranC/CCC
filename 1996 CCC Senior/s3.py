# Pattern Generator
import math

memo = {}

def generator(n, k):
    if memo.get((n,k)) != None:
        return memo[(n,k)]
    
    if k == 0:
        p = ''
        for i in range(n):
            p+='0'
        memo[(n,k)] = [p]
        return [p]
    
    if n == k:
        p = ''
        for i in range(n):
            p+='1'
        memo[(n,k)] = [p]    
        return [p]

    pat = []
    ps = generator(n-1, k-1)
    for p in ps:
        pat.append('1'+p)
    ps = generator(n-1, k)
    for p in ps:
        pat.append('0'+p)
    memo[(n,k)] = pat.copy()
    return pat
            
        
N = int(input())   
for p in range(N):
    n, k = [eval(i) for i in input().split()]
    
    print("The bit patterns are")
    pattern = generator(n, k)
    
    for i in range(len(pattern)):
        for j in range(n):
            print(pattern[i][j], sep='', end='')
        print()
    if p < N-1:
        print()
