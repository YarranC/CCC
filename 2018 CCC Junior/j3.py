# Are we there yet?

cons = [0]
last = 0
for i in input().split():
    cons.append(int(i)+last)
    last += int(i)

for i in range(len(cons)):
    for j in range(len(cons)):
        print(abs(cons[j]-cons[i]), end = ' ')
    print()
