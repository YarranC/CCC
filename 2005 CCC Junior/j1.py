# Problem J1: The Cell Sell

day = int(input())
night = int(input())
weekend = int(input())

if day > 100:
    A = (day - 100) * 0.25
else:
    A = 0

if day > 250:
    B = (day - 250) * 0.45
else:
    B = 0

A = A + 0.15 * night + 0.2 * weekend
B = B + 0.35 * night + 0.25 * weekend

print('Plan A costs', round(A, 2))
print('Plan B costs', round(B, 2))

if A > B:
    print('Plan B is cheapest.')
elif A < B:
    print('Plan A is cheapest.')
else:
    print('Plan A and B are the same price.')
