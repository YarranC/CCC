# 9966

m = int(input())
n = int(input())
rotatable = {'1':'1', '6':'9', '8':'8','9':'6', '0':'0'}


cnt = 0
for i in range(m, n+1):
    l = [c for c in str(i)]
    check = True
    for p in range(int(len(l)/2)+1):
        if l[p] not in rotatable or rotatable[l[p]] != l[len(l)-1-p]:
            check = False;
    if check:
        cnt+=1

print(cnt)
        
            
        
