# Double Dice

A = 100
D = 100

roll = int(input())

for _ in range(roll):
    a, d = input().split()
    a = int(a)
    d = int(d)
    if a > d:
        D-=a
    elif d > a:
        A-=d

print(A)
print(D)
