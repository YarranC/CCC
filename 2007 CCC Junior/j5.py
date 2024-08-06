# Problem J5: Keep on Truckin’

hotels = [0, 990, 1010, 1970, 2030, 2940, 3060,
          3930, 4060, 4970, 5030, 5990, 6010, 7000]

A = int(input())
B = int(input())

N = int(input())

for n in range(N):
    hotels.append(int(input()))

hotels.sort()

def check(a, b):
    t = []
    for h in hotels:
        if h >= a and h <= b:
            t.append(h)
    return t

memo = {}

def count(pos):
    if memo.get(pos) != None:
        return memo[pos]
    
    global A, B
    
    pa = pos + A
    pb = pos + B

    h_list = check(pa, pb)
    cnt = 0
    
    if h_list == []:
        memo[pos] = 0
        return 0
    else:
        for h in h_list:
            if h == 7000:
                cnt+=1
            else:
                cnt+= count(h)
    memo[pos] = cnt
    return cnt
            
print(count(0))
        
