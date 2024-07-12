# Exactly Electrical

a, b = input().split()
c, d = input().split()

t = int(input())

d = abs(int(c) - int(a)) + abs(int(d) - int(b))

if t < d:
    print('N')
elif t == d or t%2 == d%2:
    print('Y')
else:
    print('N')
