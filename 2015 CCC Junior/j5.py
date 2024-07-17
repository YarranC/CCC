import math

pie = int(input())
ppl = int(input())

# Dictionary to store the results of subproblems
memo = {}

def distribute(prev, piece, people):
    # Check if the result is already in the memo dictionary
    if (prev, piece, people) in memo:
        return memo[(prev, piece, people)]

    if piece == people:
        return 1
    if piece == 1:
        return 1
    if people == 1:
        return 1

    cnt = 0
    for i in range(prev, piece // people + 1):
        if int((piece - i) / (people - 1)) >= i:
            cnt += distribute(i, piece - i, people - 1)

    # Store the result in the memo dictionary
    memo[(prev, piece, people)] = cnt
    return cnt

print(distribute(1, pie, ppl))
