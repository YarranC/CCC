# Wait Time

timer = 0
receive = dict()
send = dict()
msg = []
for _ in range(int(input())):
    a, b = input().split()
    b = int(b)
    if a == 'R':
        receive[b] = timer
        msg.append(b)
        timer += 1
    elif a == 'S':
        if send.get(b) == None:
            send[b] = []
        send[b].append(timer - receive[b])
        msg.remove(b)
        timer += 1
    else:
        timer += (int(b)-1)

l = sorted(receive)

for x in l:
    if not x in msg:
        s = 0
        for i in send[x]:
            s += i
        print(x, s)
    else:
        msg.remove(x)
        print(x, '-1')

