# Problem J3: GPS Text Entry

keyboard = {}

for i in range(65, 91):
    keyboard[chr(i)] = [(i-65)//6,(i-65)%6]

keyboard[' '] = [4, 2]
keyboard['-'] = [4, 3]
keyboard['.'] = [4, 4]
keyboard['enter'] = [4, 5]

line = input()

pos = [0, 0]
cnt = 0
for c in line:
    cp = keyboard[c]
    cnt+=abs(pos[0]-cp[0])
    cnt+=abs(pos[1]-cp[1])
    pos = cp

cp = keyboard['enter']
cnt+=abs(pos[0]-cp[0])
cnt+=abs(pos[1]-cp[1])
    
print(cnt)
