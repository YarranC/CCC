# Censor

n = int(input())
for i in range(n):
    line = input().split()
    for j in range(len(line)):
        if len(line[j]) == 4:
            print('****', end='')
        else:
            print(line[j], end='')

        if j < len(line) - 1:
            print(' ', end= '')

    if i < n - 1:
        print()
