# Surfin'

n = int(input())

webs = dict()
r_webs = dict()
cnt = 0
while cnt < n:
    host = input()
    line = input()

    while '</HTML>' not in line:
        if 'HREF' in line:
            for s in line.split():
                if len(s) > 5 and s[:5] == 'HREF=':
                    t = s.split('\"')[1]
                    if webs.get(host) == None:
                        webs[host] = [t]
                    else:
                        webs[host].append(t)
                    if r_webs.get(t) == None:
                        r_webs[t] = [host]
                    else:
                        r_webs[t].append(host)
        line = input()
    cnt+=1

for a in webs.keys():
    for b in webs[a]:
        print('Link from', a, 'to', b)

memo = []
pages = []
def find(src, dest):
    global r_webs

    if r_webs.get(dest) == None:
            return False
        
    pages = r_webs[dest]
    while len(pages) >= 1:
        l = []
        for s in pages:
            if s == src:
                return True
            else:
                if r_webs.get(s) != None:
                    for t in r_webs[s]:
                        if t not in memo:
                            l.append(t)
                            memo.append(t)
        pages = l
        
        
    return False

src = input()

while src != 'The End':
    dest = input()
    memo = []
    pages = []
    if find(src, dest):
        print('Can surf from', src, 'to', dest, end='.\n')
    else:
        print('Can\'t surf from', src, 'to', dest, end='.\n')
    src = input()
        
        
