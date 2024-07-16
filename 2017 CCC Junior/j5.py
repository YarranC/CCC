# Nailed It!

N = int(input())

board = [0 for _ in range(2000)]
fence = [0 for _ in range(4000)]

pieces = input().split()

for L in pieces:
    L = int(L)
    board[L-1]+=1

for i in range(1999):
    for j in range(i, 2000):
        if i == j:
            fence[i+j+2]+=int(board[i]/2)
        else:
            fence[i+j+2]+=min(board[i], board[j])

length = 0
count = 0

for l in fence:
    if l > length:
        length = l
        count = 1
    elif l == length:
        count += 1

print(length, count)


