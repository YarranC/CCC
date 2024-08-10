# Double Knockout Competition

n = int(input())

for i in range(n):
    num = int(input())
    dkc = [num, 0, 0]

    print('Round 0:', num, 'undefeated, 0 one-loss, 0 eliminated')
    rnd = 1
    while True:
        if dkc[0] == 0 and dkc[1] == 2:
            print('Round ', rnd, ': 0 undefeated, 1 one-loss, ', num-1, ' eliminated', sep='')
            print('There are', rnd, 'rounds.')
            break
        elif dkc[0] == 1 and dkc[1] == 1:
            dkc[0] = 0
            dkc[1] = 2
            print('Round ', rnd, ': ', dkc[0], ' undefeated, ', dkc[1], ' one-loss, ', dkc[2], ' eliminated', sep='')
            rnd+=1
        else:
            a, b, c = dkc
            dkc[0] = a//2 + a%2
            dkc[1] = a//2 + b//2 + b%2
            dkc[2] += b//2
            print('Round ', rnd, ': ', dkc[0], ' undefeated, ', dkc[1], ' one-loss, ', dkc[2], ' eliminated', sep='')
            rnd+=1

    if i < n-1:
        print()