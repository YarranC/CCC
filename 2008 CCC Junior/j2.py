# Problem J2: Do the Shuffle

music = ['A', 'B', 'C', 'D', 'E']

def button1():
    global music

    m = music[0]
    music.remove(m)
    music.append(m)

def button2():
    global music

    m = music[4]
    music.remove(m)
    music.insert(0, m)

def button3():
    global music

    m = music[1]
    music.remove(m)
    music.insert(0, m)

def button4():
    global music

    print(*music)

while True:
    b = input()
    t = int(input())

    if b == '4' and t == 1:
        button4()
        import sys
        sys.exit(0)
    
    for _ in range(t):
        match b:
            case '1': button1()
            case '2': button2()
            case '3': button3()

    
    


