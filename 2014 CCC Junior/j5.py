# Assigning Partners
import sys
               
n = int(input())

A = input().split()
B = input().split()

pair = dict()

for i in range(n):
    if A[i] == B[i]:
        print('bad')
        sys.exit(0)
    else:
        if not A[i] in pair: 
            pair[A[i]] = B[i]
        if not B[i] in pair:
            pair[B[i]] = A[i]
        if A[i] in pair and pair[A[i]] != B[i]:
            print('bad')
            sys.exit(0)
        if B[i] in pair and pair[B[i]] != A[i]:
            print('bad')
            sys.exit(0)
print('good')
