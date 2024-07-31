# Problem J2: Terms of Office

gap = 3*5*4

x = int(input())
y = int(input())

for i in range(x, y+1):
    if (i-x)%gap == 0:
        print('All positions change in year', i)
