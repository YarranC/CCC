# Problem J1 - Trident

t = int(input())
s = int(input())
h = int(input())

for i in range(t):
    for _ in range(2):
        print('*', sep='', end='')
        for j in range(s):
            print(' ', sep='', end='')
    print('*')

print('*', sep='', end='')
for j in range(s):
    print('*', sep='', end='')
print('*', sep='', end='')
for j in range(s):
    print('*', sep='', end='')
print('*')

for i in range(h):
    for j in range(s+1):
        print(' ', sep='', end='')
    print('*')
