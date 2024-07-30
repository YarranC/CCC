# Problem J3/S1 - Snakes and Ladders

snakes = {54:19, 90:48, 99:77}
ladder = {9:34, 40:64, 67:86}

pos = 1

dice = int(input())

while dice>=2 and dice <=12:
    temp = pos + dice
    if temp == 100:
        print('You are now on square 100')
        print('You Win!')
        break

    if temp < 100:
        if snakes.get(temp) != None:
            temp = snakes[temp]
        if ladder.get(temp) != None:
            temp = ladder[temp]
        pos = temp

    print('You are now on square', pos)
        
    dice = int(input())

if dice < 2 or dice > 12:
    print('You Quit!')
