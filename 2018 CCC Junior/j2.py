# Occupy parking

N = int(input())

hier = input()
today = input()
cnt = 0

for i in range(N):
    if hier[i] == 'C' and today[i] == 'C':
        cnt+=1
print(cnt)
