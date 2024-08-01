# Problem J2: RSA Numbers

a = int(input())
b = int(input())

def RSA(n):
    memo = []
    f = 0
    i = 1
    while i < n:
        if n%i == 0:
            if i not in memo:
                memo.append(i)
                f+=1
            if n//i not in memo:
                memo.append(n//i)
                f+=1
        i+=1

    return (f == 4)

cnt = 0
for i in range(a, b+1):
    if RSA(i):
        cnt+=1

print('The number of RSA numbers between', a, 'and', b, 'is', cnt)
