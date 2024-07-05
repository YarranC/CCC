# Harvest Waterloo

# get size of the patch
row = int(input())
column = int(input())

# get description of the patch
patch = [['*' for i in range(column)] for j in range(row)]  

for i in range(row):
    p = input()
    patch[i] = list(p)

# get farmer initial location
ir = int(input())
ic = int(input())

Value = 0

# pickup pumpkin from patch (p) at row (r), and column (c)
def pickup(r, c):
    stack = [(r, c)]
    total_value = 0

    while stack:
        r, c = stack.pop()
        
        if r >= row or r < 0 or c >= column or c < 0 or patch[r][c] == '*':
            continue

        if patch[r][c] == 'S':
            total_value += 1
        elif patch[r][c] == 'M':
            total_value += 5
        elif patch[r][c] == 'L':
            total_value += 10

        patch[r][c] = '*'

        stack.append((r-1, c))
        stack.append((r+1, c))
        stack.append((r, c-1))
        stack.append((r, c+1))

    return total_value

# total value of all pumpkins harvested
Value += pickup(ir, ic)

print(Value)
