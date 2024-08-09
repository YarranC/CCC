# When in Rome

def rtoi(r):
    i = 0
    lc = ''
    for c in r:
        match c:
            case 'I':
                i+=1
            case 'V':
                i+=5
                if lc == 'I':
                    i-=2
            case 'X':
                i+=10
                if lc == 'I':
                    i-=2
            case 'L':
                i+=50
                if lc == 'X':
                    i-=20
            case 'C':
                i+=100
                if lc == 'X':
                    i-=20
            case 'D':
                i+=500
                if lc == 'C':
                    i-=200
            case 'M':
                i+=1000
                if lc == 'C':
                    i-=200
                    
        lc = c
        
    return i

def itor(i):
    r = ''
    
    for n in range(i//1000):
        r+='M'

    i=i%1000

    if i >= 900:
        r+='CM'
        i-=900
        
    if i >= 500:
        r+='D'
        i-=500

    if i >= 400:
        r+='CD'
        i-=400

    for n in range(i//100):
        r+='C'

    i=i%100

    if i >= 90:
        r+='XC'
        i-=90

    if i >= 50:
        r+='L'
        i-=50

    if i >= 40:
        r+='XL'
        i-=40

    for n in range(i//10):
        r+='X'

    i=i%10

    if i >= 9:
        r+='IX'
        i-=9

    if i >= 5:
        r+='V'
        i-=5

    if i >= 4:
        r+='IV'
        i-=4

    for n in range(i):
        r+='I'
        
    return r
    
for _ in range(int(input())):
    line = input()
    plus = line.index('+')
    a = rtoi(line[:plus])
    b = rtoi(line[plus+1:-1])
    s = a + b
    if s > 1000:
        print(line, 'CONCORDIA CUM VERITATE', sep='')
    else:
        print(line, itor(s), sep='')
    
