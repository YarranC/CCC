# Vote Count

_ = int(input())

A = 0
B = 0

vote = input()
for v in vote:
    if v == 'A':
        A+=1
    elif v == 'B':
        B+=1

if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')
