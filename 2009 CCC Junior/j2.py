# Problem J2: Old Fishin’ Hole

trout = int(input())
pike = int(input())
pickerel = int(input())
total = int(input())

cnt = 0
for i in range(total//trout+1):
    for j in range(total//pike+1):
        for k in range(total//pickerel+1):
            if i != 0 or j != 0 or k != 0:
                s = i * trout + j * pike + k * pickerel
                if s <= total:
                    cnt+=1
                    print(i, 'Brown Trout,', j, 'Northern Pike,', k, 'Yellow Pickerel')

print('Number of ways to catch fish:', cnt)


            
