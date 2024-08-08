# Mod Inverse

x = int(input())
m = int(input())

for n in range(m//x, m):
    for i in range(1, 101):
        if (x*n)%(m*i) == 1:
            print(n)
            import sys
            sys.exit(0)
            
print('No such integer exists.')
