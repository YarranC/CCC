# Square Pool

n = int(input()) # size of the yard
T = int(input()) # number of trees

trees = []
# find the location of all the trees
for i in range(T):
    x, y = input().split()
    x = int(x)
    y = int(y)
    trees.append((x, y))

# add yard boundary   
trees.append((0, 0))
trees.append((n+1, n+1))

# get the coordinates of every pair of trees
row,  col = set(), set()
for x, y in trees:
    for x2, y2 in trees:
        if x != x2:
            row.add(tuple(sorted((x, x2))))
        if y != y2:
            col.add(tuple(sorted((y, y2))))
            
# remove the yard boundary
trees = trees[:-2]

# Sort by the distance between the two trees
row = list(sorted(row, key=lambda row: abs(row[0] - row[1]), reverse=True))
col = list(sorted(col, key=lambda col: abs(col[0] - col[1]), reverse=True))

cnt = []
for i in range(2):
    trees = sorted(trees, key=lambda x: x[i])

    for s, e in row if i else col:
        s2, e2 = 0, abs(s - e)
        for tree in trees:
            if i and s < tree[0] < e and s2 < tree[1] < e2:
                e2 += abs(tree[1] - s2) + 1
                s2 = tree[1] + 1
            elif not i and s < tree[1] < e and s2 < tree[0] < e2:
                e2 += abs(tree[0] - s2) + 1
                s2 = tree[0] + 1

            if e2 > n + 1:
                break
        else:
            cnt.append(abs(s - e) - 1)
            break

print(max(cnt))
