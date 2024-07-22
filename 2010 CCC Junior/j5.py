# Knight Hop

init = [eval(x) for x in input().split()]
final = [eval(x) for x in input().split()]

steps = {}
notes = []
memo = []

def move(pos):
    if pos in memo:
        return
    
    memo.append(pos)
    
    x = pos[0]
    y = pos[1]
    
    if x + 1 <= 8 and y + 2 <= 8 and not (x+1,y+2) in steps:
        steps[(x+1,y+2)] = steps[(x,y)] + 1
        notes.append((x+1,y+2))
        
    if x + 2 <= 8 and y + 1 <= 8 and not (x+2,y+1) in steps:
        steps[(x+2,y+1)] = steps[(x,y)] + 1
        notes.append((x+2,y+1))
        
    if x + 2 <= 8 and y - 1 > 0 and not (x+2,y-1) in steps:
        steps[(x+2,y-1)] = steps[(x,y)] + 1
        notes.append((x+2,y-1))
        
    if x + 1 <= 8 and y - 2 > 0 and not (x+1,y-2) in steps:
        steps[(x+1,y-2)] = steps[(x,y)] + 1
        notes.append((x+1,y-2))
        
    if x - 1 > 0 and y + 2 <= 8 and not (x-1,y+2) in steps:
        steps[(x-1,y+2)] = steps[(x,y)] + 1
        notes.append((x-1,y+2))
        
    if x - 2 > 0 and y + 1 <= 8 and not (x-2,y+1) in steps:
        steps[(x-2,y+1)] = steps[(x,y)] + 1
        notes.append((x-2,y+1))
        
    if x - 2 > 0 and y - 1 > 0 and not (x-2,y-1) in steps:
        steps[(x-2,y-1)] = steps[(x,y)] + 1
        notes.append((x-2,y-1))
    if x - 1 > 0 and y - 2 > 0 and not (x-1,y-2) in steps:
        steps[(x-1,y-2)] = steps[(x,y)] + 1
        notes.append((x-1,y-2))

steps[(init[0], init[1])] = 0
notes.append((init[0], init[1]))

while len(notes) < 64:
    for n in notes:
        move(n)

print(steps[final[0], final[1]])