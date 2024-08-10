# Dynamic Dictionary Coding

n = int(input())

for _ in range(n):
    cnt = 1
    d = {}
    line = input()
    while line != '':
        line = line.split()
        for i in range(len(line)):
            word = line[i]
            if d.get(word) == None:
                print(word, end='')
                d[word] = cnt
                cnt+=1
            else:
                print(d[word], end='')
            if i < len(line)-1:
                print(' ', end='')
        print()
        line = input()
    print()
