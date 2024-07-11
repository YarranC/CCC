# Choose your own path
# failed j5.3-1 and j5.3-3 test cases

N = int(input())

status = [0 for _ in range(N)]
path = [1 for _ in range(N)]

table = dict()
for i in range(N):
    line = input().split()
    table[i+1] = line[1:]

# search path from page, return length of the path
def search(page):
    #print(page)
    # if already tried this page
    if status[page-1] == 2:
        return path[page-1]
    elif status[page-1] == 0:
        # if new page
        status[page-1] = 1
    
        # if reached end page
        if len(table[page]) == 0:
            path[page-1] = 1
            status[page-1] = 2
            return path[page-1]

        # if not end page
        l=[]
        for i in range(len(table[page])):
            l.append(search(int(table[page][i])))
        #print("page", page, l)
        path[page-1] = min(l)+1
        status[page-1] = 2
        return path[page-1]
    else:
        return N

search(1)

#print(status)
#print(path)

for i in range(N):
    if status[i] == 0:
        print('N')
        print(path[0])
        import sys
        sys.exit(0)

print('Y')
print(path[0])


