# Winning Score

Apples = 3*int(input()) + 2*int(input()) + int(input())
Bananas = 3*int(input()) + 2*int(input()) + int(input())

if Apples > Bananas:
    print('A')
elif Bananas > Apples:
    print('B')
else:
    print('T')
