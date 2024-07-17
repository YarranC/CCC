# Chances of winning

T = int(input())
G = int(input())

score = [0, 0, 0, 0]
plays = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

# calculate current scores and get the remaining games
for _ in range(G):
    a, b, sa, sb = [eval(i) for i in input().split()]
    if sa > sb:
        score[a-1] +=3
    elif sb > sa:
        score[b-1] +=3
    else:
        score[a-1] +=1
        score[b-1] +=1
    plays.remove(tuple(sorted((a,b))))

results = [0 for _ in range(len(plays))]
win = 0
game = 0
while game < pow(3, len(plays)):
    final = [i for i in score]
    for i in range(len(plays)):
        (a,b) = plays[i]

        results[i] = game // pow(3,i) % 3
        if results[i] == 0:
            final[a-1] +=3
        elif results[i] == 1:
            final[b-1] +=3
        elif results[i] == 2:
            final[a-1] +=1
            final[b-1] +=1
    if final[T-1] == max(final) and final.count(final[T-1]) == 1:      
        win+=1
    game+=1

print(win)
    
