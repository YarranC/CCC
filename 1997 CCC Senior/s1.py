# Sentences

n = int(input())

for _ in range(n):
    sn = int(input())
    vn = int(input())
    on = int(input())

    sub = []
    for _ in range(sn):
        sub.append(input())

    verb = []
    for _ in range(vn):
        verb.append(input())

    obj = []
    for _ in range(on):
        obj.append(input())

    for i in range(sn):
        for j in range(vn):
            for k in range(on):
                print(sub[i], verb[j], obj[k], end='.\n')

    print()
