# Babbling Brooks

stream = []
for i in range(int(input())):
    stream.append(int(input()))

flow = input()
while flow != '77':
    if flow == '99':
        s = int(input())-1
        p = eval(input())/100
        t = stream[s]
        stream[s] = t*p
        stream.insert(s+1, t*(1-p))

    if flow == '88':
        s = int(input())-1
        stream[s]+=stream[s+1]
        stream.pop(s+1)

    flow = input()

for i in range(len(stream)):
    stream[i] = int(stream[i])
print(*stream)
