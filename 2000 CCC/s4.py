# Golf

distance = int(input())
num = int(input())

clubs = []
for i in range(num):
    clubs.append(int(input()))

# Initialize a list to store the minimum strokes needed to reach each distance
dp = [float('inf')] * (distance + 1)
dp[0] = 0  # Base case: 0 strokes needed to reach distance 0

# Iterate through each distance from 1 to the target distance
for d in range(1, distance + 1):
    for c in clubs:
        if d >= c:
            dp[d] = min(dp[d], dp[d - c] + 1)

# Check if it's possible to reach the target distance
if dp[distance] == float('inf'):
    print('Roberta acknowledges defeat.')
else:
    print('Roberta wins in', dp[distance], 'strokes.')
