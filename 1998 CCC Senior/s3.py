# Mars Rover 

pos = [0, 0]
direction = 0

num = int(input())
for i in range(num):
    cmd = input()
    pos = [0, 0]
    direction = 0
    while cmd != '0':
        match cmd:
            case '1':
                dist = int(input())
                match direction:
                    case 0:
                        pos[1]+=dist
                    case 1:
                        pos[0]+=dist
                    case 2:
                        pos[1]-=dist
                    case 3:
                        pos[0]-=dist
            case '2':
                direction = (direction + 1) % 4
            case '3':
                direction = (direction - 1) % 4
        cmd = input()

    print('Distance is', abs(pos[0]) + abs(pos[1]))

    if abs(pos[0]) + abs(pos[1]) != 0:
        match direction:
            case 0:
                if pos[1] >= 0 and pos[0] > 0:
                    print(3)
                    direction = 3
                if pos[1] >= 0 and pos[0] < 0:
                    print(2)
                    direction = 1
                if pos[1] > 0 and pos[0] == 0:
                    print(3)
                    print(3)
                    direction = 2
            case 1:
                if pos[0] >= 0 and pos[1] > 0:
                    print(2)
                    direction = 2
                if pos[0] >= 0 and pos[1] < 0:
                    print(3)
                    direction = 0
                if pos[0] > 0 and pos[1] == 0:
                    print(3)
                    print(3)
                    direction = 3
            case 2:
                if pos[1] <= 0 and pos[0] < 0:
                    print(3)
                    direction = 1
                if pos[1] <= 0 and pos[0] > 0:
                    print(2)
                    direction = 3
                if pos[1] < 0 and pos[0] == 0:
                    print(3)
                    print(3)
                    direction = 0
            case 3:
                if pos[0] <= 0 and pos[1] > 0:
                    print(3)
                    direction = 2
                if pos[0] <= 0 and pos[1] < 0:
                    print(2)
                    direction = 0
                if pos[0] < 0 and pos[1] == 0:
                    print(3)
                    print(3)
                    direciton = 1
        
        if direction == 0 or direction == 2:
            if pos[1] != 0:
                print(1)
                print(abs(pos[1]))
            if pos[0]*pos[1] < 0:
                print(3)
            elif pos[0] != 0:
                print(2)
            if pos[0] != 0:
                print(1)
                print(abs(pos[0]))             

        if direction == 3 or direction == 1:
            if pos[0] != 0:
                print(1)
                print(abs(pos[0]))
            if pos[0]*pos[1] < 0:
                print(2)
            elif pos[0] != 0:
                print(3)
            if pos[1] != 0:
                print(1)
                print(abs(pos[1]))

    if i < num - 1:
        print()
