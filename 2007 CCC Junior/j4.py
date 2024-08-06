# Problem J4: Anagram Checker

p1 = input()
p2 = input()
    
len1 = len(p1)
len2 = len(p2)

cnt1 = {}
cnt2 = {}

for i in range(65, 91):
    cnt1[chr(i)] = 0
    cnt2[chr(i)] = 0

for p in p1:
    if p != ' ':
        cnt1[p]+=1
    
for p in p2:
    if p != ' ':
        cnt2[p]+=1

if cnt1 == cnt2:
    print('Is an anagram.')
else:
    print('Is not an anagram.')
