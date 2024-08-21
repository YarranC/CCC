# Slot Machines

q = int(input())
j = []

for i in range(3):
    j.append(int(input()))

N = 1
P = 0
while True:
    if q <= 0:
        print(f"Martha plays {P} times before going broke.")
        break
    if N == 1:
        if j[N - 1] == 34:
            j[N - 1] = 0
            q += 29
        else:
            j[N - 1] += 1
            q -= 1
        N = 2
        P += 1
    elif N == 2:
        if j[N - 1] == 99:
            j[N - 1] = 0
            q += 59
        else:
            j[N - 1] += 1
            q -= 1
        N = 3
        P += 1
    elif N == 3:
        if j[N - 1] == 9:
            j[N - 1] = 0
            q += 8
        else:
            j[N - 1] += 1
            q -= 1
        N = 1
        P += 1