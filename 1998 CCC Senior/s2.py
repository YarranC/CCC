# Cross Number Puzzle

def perfect(num):
    factor = [1]
    for f in range(2, num//2+1):
        if num%f == 0 and f not in factor:
            factor.append(f)
            factor.append(num//f)
    s = 0
    for i in range(len(factor)):
        s+=factor[i]

    if s == num:
        print(num)

def cube_sum(num):
    s = 0
    t = num
    while t > 0:
        s += pow(t%10, 3)
        t = t//10
       
    if s == num:
        print(num)
        
for i in range(1000, 10000):
    perfect(i)
print()
for i in range(100, 1000):
    cube_sum(i)
    
