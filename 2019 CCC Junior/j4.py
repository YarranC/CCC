# Flipper

grid = [[1,2],[3,4]]

for c in input():
    if c == 'H':
        temp = [grid[1], grid[0]]
        grid = temp
    else:
        temp = [[grid[0][1], grid[0][0]], [grid[1][1], grid[1][0]]]
        grid = temp

print(*grid[0], sep=' ')
print(*grid[1], sep=' ')
