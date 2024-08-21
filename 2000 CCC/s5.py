# sheep and coyotes

sheeps = []
eaten = []

for _ in range(int(input())):
    sheeps.append([int(float(input())*100), int(float(input())*100)])

sheeps.sort()

for s in sheeps:
    d = pow(s[1], 2)
    e = s
    for t in sheeps:
        dd = pow(abs(t[0] - s[0]), 2) + pow(t[1], 2)
        if dd <= d:
            d = dd
            e = t

    if e not in eaten:
        eaten.append(e)

for s in eaten:
    print('The sheep at (', format(s[0]/100,'.2f'), ', ', format(s[1]/100,'.2f'), ') might be eaten.', sep='')
        
               
