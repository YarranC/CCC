# Maximum Distance

for _ in range(int(input())):
    n = int(input())
    seq_x = [eval(i) for i in input().split()]
    seq_y = [eval(i) for i in input().split()]

    max_dist = 0
    
    for i in range(n):
        for j in range(1, n-i+1):
            if seq_y[n-j] >= seq_x[i]:
              break
        max_dist = max(max_dist, n-j-i)

    print('The maximum distance is', max_dist)
