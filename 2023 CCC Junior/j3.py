# Special Event

n=int(input())
f=[0] * 5
for x in range(n):
    a=input()
    for y in range(5):
        if a[y]=="Y":
            f[y]+=1
p=[]
o=max(f)
for z in range(5):
    if f[z]==o:
        p.append(z+1)
print(*p, sep = ",")
