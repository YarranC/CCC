# Strategic Bombing

road = {'A':[], 'B':[]}
pair = []
link = input()
while link != '**':
    a = link[0]
    b = link[1]

    pair.append(link)
    
    if road.get(a) == None:
        road[a] = [b]
    else:
        road[a].append(b)

    if road.get(b) == None:
        road[b] = [a]
    else:
        road[b].append(a)
        
    link = input()
    
paths = []

def find(x, y, p):
    if x in p: return
    
    if y in road[x]:
        p.append(x)
        p.append(y)
        paths.append(p.copy())     
        p.remove(x)
        p.remove(y)
        
        for c in road[x]:
            if c != y:
               p.append(x)
               find(c, y, p)
               p.remove(x)
        return 

    for c in road[x]:
        if c not in p:
            p.append(x)
            find(c, y, p)
            p.remove(x)      

find('A', 'B', [])

cp = pair.copy()
for p in paths:
    ps = ''
    for c in p:
        ps+=c

    for i in pair:
        if not i in ps and not (i[1]+i[0]) in ps:
            if i in cp:
                cp.remove(i)

for p in cp: print(p)
print('There are', len(cp), 'disconnecting roads.')
        
