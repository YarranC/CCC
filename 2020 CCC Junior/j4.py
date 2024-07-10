# Cyclic Shifts

T = input()
S = input()
f = False

for _ in range(len(S)):
    if S in T:
        print("yes")
        f = True
        break
    else:
        S = S[1:]+S[0]
if f == False:
    print("no")
