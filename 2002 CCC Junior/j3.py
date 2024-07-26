# Problem S1J3 - The Students’ Council Breakfast

prices = []
# Pink, Green, Red, orange
prices.append(int(input()))
prices.append(int(input()))
prices.append(int(input()))
prices.append(int(input()))

# target total
total = int(input())

# minimum number of tickets
m = 9999999

# number of combinations
count = 0

for p in range(int(total/prices[0])+1):
    for g in range(int(total/prices[1])+1):
        for r in range(int(total/prices[2])+1):
            for o in range(int(total/prices[3])+1):
                if (p*prices[0] + g*prices[1] + r*prices[2] + o*prices[3]) == total:
                    print('# of PINK is ', p, ' # of GREEN is ', g, ' # of RED is ', r, ' # of ORANGE is ', o, sep='')
                    m = min(m, p+g+r+o)
                    count += 1
                    
print('Total combinations is ', count, '.', sep='')
print('Minimum number of tickets to print is ', m, '.', sep='')
