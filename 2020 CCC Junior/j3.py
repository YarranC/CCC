# Art

N = int(input())

x=[]
y=[]
for _ in range(N):
    a,b = input().split(',')
    x.append(int(a))
    y.append(int(b))
    x.sort()
    y.sort()
    
print(x[0]-1, y[0]-1, sep=",")
print(x[N-1]+1, y[N-1]+1, sep=",")