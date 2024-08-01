# Problem J4: Cross Spiral

width = int(input())
height = int(input())

grid =[[0 for _ in range(width)] for _ in range(height)]

cw = int(input())
ch = int(input())

for i in range(cw):
    for j in range(ch):
        grid[j][i] = 1
        grid[j][width-i-1] = 1
        grid[height-j-1][i] = 1
        grid[height-j-1][width-i-1] = 1

steps = int(input())

h = 0
w = cw
cnt = 0
move = True
grid[h][w] = 1

while move and cnt < steps:
    # top left quarter 
    if h >= 0 and h < height//2 and w >= 0 and w < width//2:
        # move up
        if h - 1 >= 0 and grid[h-1][w] != 1:
            h-=1
            grid[h][w] = 1
            cnt+=1
        # move right
        elif w + 1 < width and grid[h][w+1] != 1:
            w+=1
            grid[h][w] = 1
            cnt+=1
        else:
            move = False
            
    # top right quarter 
    elif h >= 0 and h < height//2 and w >= width//2 and w < width:
        # move right
        if w + 1 < width and grid[h][w+1] != 1:
            w+=1
            grid[h][w] = 1
            cnt+=1
        # move down
        elif h + 1 < height and grid[h+1][w] != 1:
            h+=1
            grid[h][w] = 1
            cnt+=1
        else:
            move = False

    # bottom right quarter 
    elif h >= height//2 and h < height and w >= width//2 and w < width:
        # move down
        if h + 1 < height and grid[h+1][w] != 1:
            h+=1
            grid[h][w] = 1
            cnt+=1
        # move left
        elif w - 1 >= 0 and grid[h][w-1] != 1:
            w-=1
            grid[h][w] = 1
            cnt+=1
        else:
            move = False

    # bottom left quarter 
    if h >= height//2 and h < height and w >= 0 and w < width//2:
        # move left
        if w - 1 >= 0 and grid[h][w-1] != 1:
            w-=1
            grid[h][w] = 1
            cnt+=1
        # move up
        elif h - 1 >= 0 and grid[h-1][w] != 1:
            h-=1
            grid[h][w] = 1
            cnt+=1
        
        else:
            move = False
    

print(w+1)
print(h+1)
