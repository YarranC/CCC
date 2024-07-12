# Tournament Selection
cnt = 0
for _ in range(6):
    if input() == 'W':
       cnt+=1

match cnt:
    case 5 | 6:
        print(1)
    case 3 | 4:
        print(2)
    case 1 | 2:
        print(3)
    case _:
        print(-1)
