# Problem J5: Nukit


reactions = [[2, 1, 0, 2], [1, 1, 1, 1], [0, 0, 2, 1], [0, 3, 0, 0], [1, 0, 0, 1]]
memo = {True:[], False:[]}
def check(parts, player): 
    if [parts, player] in memo[True]:
        return True
    elif [parts, player] in memo[False]:
        return False
    
    for r in reactions:
        t = [parts[0]-r[0], parts[1]-r[1], parts[2]-r[2], parts[3]-r[3]]
        #print(' ', parts, r, t)
        if t[0] >= 0 and t[1] >= 0 and t[2] >= 0 and t[3] >= 0 and not check(t, (player+1)%2):
            memo[True].append([parts, player])
            return True
        #print(' ', parts, r, t, result)

    memo[False].append([parts, player])
    return False

for _ in range(int(input())):
    parts = [eval(i) for i in input().split()]

    if check(parts, 0):
        print("Patrick")
    else:
        print("Roland")