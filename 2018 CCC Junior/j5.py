# Choose your own path

N = int(input())

visited = [1]
end = []
reached = [1]
table = dict()

for i in range(N):
    line = input().split()
    if int(line[0]) == 0:
        end.append(i+1)
        if not i+1 in reached:
            reached.append(i+1)
    else:
        for p in line[1:]:
            p = int(p)
            if p != i+1:
                if not p in reached:
                    reached.append(p)
                if table.get(p) == None:
                   table[p] = [i+1]
                else:
                    table[p].append(i+1)

if len(reached) == N:
    print('Y')
else:
    print('N')

cnt = 1
while len(end) >= 1:

    l = []
    for p in end:
        if table.get(p) != None:
            src = table[p]
            for s in src:
                if s == 1:
                    print(cnt+1)
                    import sys
                    sys.exit(0)
                if not s in visited:
                    visited.append(s)
                    l.append(s)
    end = l
    cnt+=1
