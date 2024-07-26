# Problem S2J4 - Fraction Action

n = int(input())
d = int(input())

if n == 0:
    print(0)
    import sys
    sys.exit(0)
    
w = int(n/d)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = n - w*d
g = gcd(n, d)

if w != 0 and n == 0:
    print(w)

if w == 0 and n != 0:
    print(int(n/g), '/', int(d/g), sep='')

if w != 0 and n != 0:
    print(w, ' ', int(n/g), '/', int(d/g), sep='')
