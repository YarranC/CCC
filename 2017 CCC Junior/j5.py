# Nailed It! 
# works for N <= 1000, need to improve time efficiency

N = int(input())
L = input().split()

length = 0
temp_h = []
height = dict()
status = dict()

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        h = int(L[i]) + int(L[j])
        if height.get(h) == None:
            height[h] = 1
            status[h] = []
            status[h].append(i)
            status[h].append(j)
            if height[h] == length:
                cnt+=1
                temp_h.append(h)
        else:
            a = j in status[h]
            b = i in status[h]

            if not a and not b:
                height[h]+=1
                status[h].append(i)
                status[h].append(j)
                if height[h] == length:
                    cnt+=1
                    temp_h.append(h)
        if height[h] > length:
            length = height[h]
            cnt = 1
            temp_h = [h]

print(length, cnt)
