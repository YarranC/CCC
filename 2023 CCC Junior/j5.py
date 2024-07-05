# CCC Word Hunt

word = input() # word to be serached for
    
row = int(input()) # number of rows
col = int(input()) # number of columns

# get the grid
grid = [[] for i in range(row)]
    
for i in range(row):
    grid[i] = input().split()
    
# find the word
count = 0

def turn(d, t):
    return (d + t + 360)%360

def nextx(x, d):
    match d:
        case 0 | 180:
            return x
        case 270 | 315 | 225:
            return x-1
        case 90 | 45 | 135:
            return x+1

def nexty(y, d):
    match d:
        case 270 | 90:
            return y
        case 180 | 225 | 135:
            return y-1
        case 0 | 315 | 45:
            return y+1
        
# parameter coordinate x, coordinate y, index in word, direction, segment
def find(x, y, i, d, s):

    # if coordinate out of range, return 0
    if x == row or x < 0 or y == col or y < 0:
        return 0
      
    # if not matching, return 0
    if grid[x][y] != word[i]:
        return 0
    
    # if matched the last letter, return 1
    if i == len(word)-1 and grid[x][y] == word[i]:
        return 1

    c = 0
    if grid[x][y] == word[i]:
        
        # continue the same direction
        t = find(nextx(x,d), nexty(y,d), i+1, d, s)

        # if found the letter
        if t > 0:
            c+=t
            
        # if already on 2nd segment, don't try other directions
        if s == 1:
            return c
            
        # if still on 1st segment, try other directions
        if i != 0:
            d2 = turn(d, -90)
            c+=find(nextx(x,d2), nexty(y,d2), i+1, d2, 1)
                
            d2 = turn(d, 90)
            c+=find(nextx(x,d2), nexty(y,d2), i+1, d2, 1)
            
        # if it is the first letter, turn 45 degrees and try again
        else:
            for m in range(7):
                d2 = turn(d, (m+1)*45)
                c+= find(nextx(x,d2), nexty(y,d2), i+1, d2, 0)
               
    return c


count = 0
for i in range(row):
    for j in range(col):
        count += find(i, j, 0, 0, 0)

print(count)


