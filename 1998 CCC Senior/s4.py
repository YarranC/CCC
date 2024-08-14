# Lottery

def left(eq, n):
    cnt = 0
    for i in range(n):
        if eq[n-i-1] == ')':
            cnt += 1
        elif eq[n-i-1] == '(':
            cnt -= 1
        if cnt == 0 and eq[n-i-1] != 'X' :
            return n-i-1

def right(eq, n):
    cnt = 0
    for i in range(1, len(eq)-n):
        if eq[n+i] == '(':
            cnt += 1
        elif eq[n+i] == ')':
            cnt -= 1
        if cnt == 0:
            return n+i
              
n = int(input())

for i in range(n):
    eq = input().split()

    ml = []
    for j in range(len(eq)):
        if eq[j] == 'X':
            ml.append(j)
    
    t = 0
    for m in ml:
        l = left(eq, m+t)
        eq.insert(l, '(')
        r = right(eq, m+t+1)
        eq.insert(r+1, ')')
        t+=2    

    ps = []
    for j in range(len(eq)):
        if eq[j] == '+' or eq[j] == '-':
            ps.append(j)

    if len(ps) == 0:
        eq = eq[1:-1]
        
    t = 0
    tp = ps.copy()
    c = 0
    while len(tp) > 1:
        k = ps[c]
        tp.remove(k)
        l = left(eq, k+t)
        eq.insert(l, '(')
        r = right(eq, k+t+1)
        eq.insert(r+1, ')')
        t+=2
        c+=1
        
    for p in range(len(eq)):
        print(eq[p], sep='', end='')
        if p+1 < len(eq) and eq[p+1] != ')' and eq[p] != '(':
            print(' ', end='')
    print()
    
    if i < n - 1:
        print()
