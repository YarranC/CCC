# Epidemiology

P = int(input())
N = int(input())
R = int(input())

total = N
last = N
day = 0
while total <= P:
    total+=last*R
    last = last*R
    day+=1

print(day)
