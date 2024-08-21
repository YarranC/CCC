# Card Game

def check(c):
    #print('check', c)
    match c:
        case 'jack' | 'queen' | 'king' | 'ace':
            return True
        case _:
            return False
        
score = [0, 0]
player = 0
card = []
for _ in range(52):
    card.append(input())

i = 0
while i < 52:
    A, B = score
    #print(i, card[i], A, B)
    match card[i]:
        case 'ace':
            if i < 52-4:
                found = False
                for j in range(1, 5):
                   if check(card[i+j]):
                       found = True
                       break
                if not found:
                    score[player]+=4
                    i+=5
                else:
                    i+=j
            else:
                i+=1
        case 'king':
            if i < 52-3:
                found = False
                for j in range(1, 4):
                   if check(card[i+j]):
                       found = True
                       break
                if not found:
                    score[player]+=3
                    i+=4
                else:
                    i+=j
            else:
                i+=1
        case 'queen':
            if i < 52-2:
                found = False
                for j in range(1, 3):
                   if check(card[i+j]):
                       found = True
                       break
                if not found:
                    score[player]+=2
                    i+=3
                else:
                    i+=j
            else:
                i+=1
        case 'jack':
            if i < 52-1:
                for j in range(1, 2):
                    if not check(card[i+j]):
                        score[player]+=1
                        i+=2
                    else:
                        i+=1
            else:
                i+=1
        case _:
            i+=1
                    
    if score[0] > A:
        print('Player A', 'scores', score[0]-A, 'point(s).')
    if score[1] > B:
        print('Player B', 'scores', score[1]-B, 'point(s).')

    player = i % 2

print('Player A:', score[0], 'point(s).')
print('Player B:', score[1], 'point(s).')
