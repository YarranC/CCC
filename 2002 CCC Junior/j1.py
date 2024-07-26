# Problem J1 - 0123456789

seven_seg = [[0 for _ in range(7)] for _ in range(10)]

seven_seg[0] = [1, 1, 1, 0, 1, 1, 1]
seven_seg[1] = [0, 0, 1, 0, 0, 1, 0]
seven_seg[2] = [1, 0, 1, 1, 1, 0, 1]
seven_seg[3] = [1, 0, 1, 1, 0, 1, 1]
seven_seg[4] = [0, 1, 1, 1, 0, 1, 0]
seven_seg[5] = [1, 1, 0, 1, 0, 1, 1]
seven_seg[6] = [1, 1, 0, 1, 1, 1, 1]
seven_seg[7] = [1, 0, 1, 0, 0, 1, 0]
seven_seg[8] = [1, 1, 1, 1, 1, 1, 1]
seven_seg[9] = [1, 1, 1, 1, 0, 1, 1]

disp = seven_seg[int(input())]

if disp[0] == 1:
    print(' * * *')
else:
    print()
    
for _ in range(3):
    if disp[1] == 1 and disp[2] == 0:
        print('*')
    elif disp[1] == 1 and disp[2] == 1:
        print('*     *')
    elif disp[1] == 0 and disp[2] == 1:
        print('      *')

if disp[3] == 1:
    print(' * * *')
else:
    print()
    
for _ in range(3):
    if disp[4] == 1 and disp[5] == 0:
        print('*')
    elif disp[4] == 1 and disp[5] == 1:
        print('*     *')
    elif disp[4] == 0 and disp[5] == 1:
        print('      *')

if disp[6] == 1:
        print(' * * *')
else:
    print()
