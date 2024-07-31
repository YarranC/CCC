# Problem J4: A Simple Encryption Algorithm

base = ord('A')
last = ord('Z')

key = input()
in_str = input()

keys=[]
for i in range(len(key)):
    keys.append(ord(key[i])-base)

out_str = ''
cnt = 0
for i in range(len(in_str)):
    s = ord(in_str[i])
    if s >= base and s <= last:
        t = s + keys[cnt%len(keys)]
        if t > last:
            t-=26
        out_str+=chr(t)
        cnt+=1

print(out_str)
