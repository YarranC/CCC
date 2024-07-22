# Global Warming
temp = [eval(x) for x in input().split()]

def check(c, s):
    i = 0      
    for n in range(len(s)):
        if s[n] != c[i]:
            return False, n
        else:
            i = (i+1)%(len(c))
    return True, 0

diff = []
while temp[0] > 0:
    if temp[0] == 1:
        print(0)
    elif temp[0] == 2:
        print(1)
    else:
        diff = []
        m = temp[1]
        for n in temp[2:]:
            diff.append(n-m)
            m = n

        if not diff[0] in diff[1:]:
            print(len(diff))
        else:
            cycle = diff[1:].index(diff[0]) + 1

            done = 0
            while done == 0:
                r, i = check(diff[:cycle], diff[cycle:])
                if r == True:
                    print(cycle)
                    done = 1
                else:
                    cycle = cycle + i + 1
                    
    temp = [eval(x) for x in input().split()]
