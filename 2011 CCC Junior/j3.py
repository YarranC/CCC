# Sumac Sequences

t = [int(input()), int(input())]

i = 1
while t[i] <= t[i-1]:
    new = t[i-1]-t[i]
    if new >= 0:
        t.append(t[i-1]-t[i])
    else:
        break
    i+=1

print(len(t))
