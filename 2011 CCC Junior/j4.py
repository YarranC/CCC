# Boring Business

plan = [[0 for _ in range(200)] for _ in range(400)]

def line(start, end):
    global init
    if start[0] != end[0]:
        x = sorted([start[0], end[0]])
        for i in range(x[0], x[1]+1):
            if plan[i+20][abs(end[1])-1] != 1:
                plan[i+20][abs(end[1])-1] = 1
            else:
                return False
    else:
        y = sorted([start[1], end[1]])
        for i in range(y[0], y[1]+1):
            if plan[end[0]+20][abs(i)-1] != 1:
                plan[end[0]+20][abs(i)-1] = 1
            else:
                return False
    return True

init = (0, -1)
def draw(direction, unit):
    global init
    match direction:
        case 'l':
            result = line((init[0], init[1]), (init[0] - unit, init[1]))
            init = (init[0] - unit, init[1])
        case 'r':
            result = line((init[0], init[1]), (init[0] + unit, init[1]))
            init = (init[0] + unit, init[1])
        case 'u':
            result = line(init, (init[0], init[1] + unit))
            init = (init[0], init[1] + unit)
        case 'd':
            result = line(init, (init[0], init[1] - unit))
            init = (init[0], init[1] - unit)
    if result == False:
        print(init[0], init[1], 'DANGER')
        import sys
        sys.exit(0)
    plan[init[0]+20][abs(init[1])-1] = 0

draw('d', 2)
draw('r', 3)
draw('d', 2)
draw('r', 2)
draw('u', 2)
draw('r', 2)
draw('d', 4)
draw('l', 8)
draw('u', 2)

d, m = input().split()
m = int(m)
while d != 'q':
    draw(d, m)
    print(init[0], init[1], 'safe')
    d, m = input().split()
    m = int(m)
