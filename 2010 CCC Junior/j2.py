# Up and Down

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

N = int(s / (a + b)) * (a - b)
nr = s % (a + b)
if nr <= a:
    N += nr
else:
    N += (2 * a - nr)

B = int(s / (c + d)) * (c - d)
br = s % (c + d)
if nr <= c:
    B += br
else:
    B += (2 * c - br)

if N > B:
    print('Nikky')
elif N < B:
    print('Byron')
else:
    print('Tied')
