# Problem J2 - Picture Perfect

c = int(input())

while c != 0:
    peri = 1024
    dime = [1, 1]
    for i in range(1, 65001):
        j = c//i
        if i*j == c:
            t = 2*i + 2*j
            if t < peri:
                peri = t
                dime = [i, j]

    dime.sort()
    print("Minimum perimeter is", peri, "with dimensions", dime[0], 'x', dime[1]) 
    
    c = int(input())
