# Cold Compress

for _ in range(int(input())):
    line = input()
    i = 1
    c = line[0]
    cnt = 1
    while i < len(line):
        if line[i] == c:
            cnt+=1
        else:
            print(cnt, end=' ')
            print(c, end=' ')
            c = line[i]
            cnt = 1
        i+=1
    print(cnt, end=' ')
    print(c)

