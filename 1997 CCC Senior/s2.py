# Nasty Numbers

for _ in range(int(input())):
    num = int(input())
    
    fac1 = [1]
    fac2 = [num]
    for i in range(2, num//2):
        if i not in fac1 and i not in fac2 and num%i == 0:
            fac1.append(min(i, num//i))
            fac2.append(max(i, num//i))

    found = False
    for i in range(len(fac1)):
        for j in range(i+1, len(fac1)):
            if fac2[i] - fac1[i] == fac2[j] + fac1[j] or fac2[i] + fac1[i] == fac2[j] - fac1[j]:
                found = True
                break
        if found:
            break

    if found:
        print(num, 'is nasty')
    else:
        print(num, 'is not nasty')
                
