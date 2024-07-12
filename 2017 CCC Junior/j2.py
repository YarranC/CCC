# Shifty Sum
N = int(input())

S = N
k = 10

for _ in range(int(input())):
    S += (N*k)
    k = (k*10)

print(S)
