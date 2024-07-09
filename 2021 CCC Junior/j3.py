# Secret Instructions

i = input()
d = "right"
while i != "99999":
    c = (int(i[0])+int(i[1]))
    if c != 0 and c % 2 == 1:
        d = "left"
    elif c != 0 and c % 2 == 0:
        d = "right"
    print(d, i[2:])
    i = input()
