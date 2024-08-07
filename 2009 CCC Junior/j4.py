# CCC '09 J4 - Signage

signs = ['WELCOME', 'TO', 'CCC', 'GOOD', 'LUCK', 'TODAY']
lengths = [7, 2, 3, 4, 4, 5]

w = int(input())

def CCC(sign, length):
    global w

    l = 0
    cnt = len(sign)
    for i in range(len(sign)):
        l+=length[i]

        if l > w:
            cnt = i
            break
        l+=1

    l = 0
    for i in range(cnt):
        l+=length[i]

    blank = w - l
    space = cnt - 1

    for i in range(cnt):
        print(sign[i], sep='', end='')
        if space != 0:
            t = blank//space
            if blank%space != 0:
                t+=1
                if i < blank%space:  
                    for j in range(t):
                        print('.', sep='', end='')
                elif i < cnt-1:
                    for j in range(t-1):
                        print('.', sep='', end='')
            else:
                if i < cnt-1:
                    for j in range(t):
                          print('.', sep='', end='')
        else:
            for j in range(blank):
                print('.', sep='', end='')

    print()

    sign = sign[cnt:]
    length = length[cnt:]

    if len(sign) != 0:
        CCC(sign, length)

CCC(signs, lengths)



