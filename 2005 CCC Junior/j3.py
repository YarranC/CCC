# Problem J3: Returning Home

moves = []

i = input()
while i != 'SCHOOL':
    moves.append(i)
    i = input()

m = len(moves)-1
while m >= 0:
    if moves[m] == 'R':
        print('Turn LEFT ', end='')
    elif moves[m] == 'L':
        print('Turn RIGHT ', end='')

    m-=1
    if m < 0:
        print('into your HOME.')
    else:
        print('onto', moves[m], 'street.')
        m-=1
