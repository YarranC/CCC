## Square Pool

N = int(input()) # size of the yard
M = N # starting with a pool of size of the yard
    
# find the location of all the trees
trees =[]
for i in range(int(input())):
    x, y = input().split()
    trees.append([int(x)-1, int(y)-1])
trees = sorted(trees)

def check(x, y, s): 
    for tree in trees:
        if x <= tree[0] and tree[0] < x+s and y <= tree[1] and tree[1] < y+s:
            return 1
    return 0

f = False
while M > 0:
    if f: break
    for i in range(N-M+1):
        if f: break
        for j in range(N-M+1):
            # check if there is tree in range
            #print(i,j,M)
            if check(i, j, M) == 0:
                print(M)
                f = True
                break
    M-=1 
