# Punchy

A, B = (0, 0)

def one(x, n):
    global A, B
    if x == 'A':
        A = n
    elif x == 'B':
        B = n

def two(x):
    global A, B
    if x == 'A':
        print(A)
    else:
        print(B)

def three(x, y):
    global A, B
    if x == 'A' and y == 'A':
        A = A + A
    elif x == 'A' and y == 'B':
        A = A + B
    elif x == 'B' and y == 'A':
        B = B + A
    elif x == 'B' and y == 'B':
        B = B + B

def four(x, y):
    global A, B
    if x == 'A' and y == 'A':
        A = A * A
    elif x == 'A' and y == 'B':
        A = A * B
    elif x == 'B' and y == 'A':
        B = B * A
    elif x == 'B' and y == 'B':
        B = B * B

def five(x, y):
    global A, B
    if x == 'A' and y == 'A':
        A = A - A
    elif x == 'A' and y == 'B':
        A = A - B
    elif x == 'B' and y == 'A':
        B = B - A
    elif x == 'B' and y == 'B':
        B = B - B

def six(x, y):
    global A, B
    if x == 'A' and y == 'A':
        A = int(A / A)
    elif x == 'A' and y == 'B':
        A = int(A / B)
    elif x == 'B' and y == 'A':
        B = int(B / A)
    elif x == 'B' and y == 'B':
        B = int(B / B)

i = input().split()

while i[0] != '7':
    match i[0]:
        case '1':
            one(i[1], int(i[2]))
        case '2':
            two(i[1])
        case '3':
            three(i[1], i[2])
        case '4':
            four(i[1], i[2])
        case '5':
            five(i[1], i[2])
        case '6':
            six(i[1], i[2])
    i = input().split()

