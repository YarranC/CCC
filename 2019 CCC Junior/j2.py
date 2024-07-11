# Time to Decompress

for _ in range(int(input())):
    i, c = input().split()
    p = []
    for _ in range(int(i)):
        p.append(c)
    print(*p, sep = "")