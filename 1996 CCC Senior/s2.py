# Divisibility by 11

def check(num):
    if num > 9:
        print(num)
    if num == 11:
        return True
    elif num > 11:
        ud = num%10
        t = num//10
        return check(t-ud)
    else:
        return False

cnt = int(input())      
for i in range(cnt):
    num = int(input())
    if check(num):
        print('The number', num, 'is divisible by 11.')
    else:
        print('The number', num, 'is not divisible by 11.')
    if i < cnt-1:
        print()


        
