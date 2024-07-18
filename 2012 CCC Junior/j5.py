# A Coin Game
# based on https://mmhs.ca/ccc/2012/s42012_kl.txt

n = 0
visited = []

class Node:
    def __init__(self, m, l):
        self.m = m
        self.level = l
        
def done(move):
    global n
    i = 0
    while i < n and move[i] == str(i+1):
        i = i + 1
    return i == n 

def movetoBaseN(move):
    global n
    basen = 0
    for i in range(n):
        for j in range (len(move[i])):
            x = int(move[i][j]) - 1
            basen += i * pow(n, x)
    return basen

#creates a new move, given an oldmove and two positions,
# p1 is the position to take from, p2 - add to
def createNewMove(oldmove, p1, p2):
    global n
    newmove = []
    for i in range (n):
        newmove.append(oldmove[i])
        
    newmove[p2] = newmove[p1][0:1] + newmove[p2]
    newmove[p1] = newmove[p1][1:]

    # don't allow big guy to move left
    if p2 < p1 and newmove[p2][0:1] == str(n):
        return oldmove
    else:
        return newmove
                                                
def search(coins):
    global n
    if done(coins):
        return 0
    else:
        tree = []
        tree.append(Node(coins,0))          
        while len(tree) > 0:   
            x = tree.pop(0)
            for i in range(n):
                # move right
                if i < n-1:
                    if len(x.m[i+1]) == 0 or x.m[i][0:1] < x.m[i+1][0:1]:
                        newmove = createNewMove(x.m, i, i+1)
                        bn = movetoBaseN (newmove)
                        if not visited[bn]:
                            visited[bn] = True
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1
                # move left
                if i > 0:
                    if len(x.m[i-1]) == 0 or x.m[i][0:1] < x.m[i-1][0:1]:
                        newmove = createNewMove(x.m, i, i-1)
                        bn = movetoBaseN (newmove)
                        if not visited[bn]:
                            visited[bn] = True
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1
                          
        return "IMPOSSIBLE"     
       
n = int(input())
while n > 0:
    coins = input().split()
    if n == 1:
        print(0)
    elif n == 2:
        a, b = [eval(i) for i in coins]
        if a > b:
            print('IMPOSSIBLE')
        else:
            print(0)
    else:
        # create and initialize a visited array
        # of all possible moves to false
        visited = [False for _ in range(pow(n,n)+1)]
        print(search(coins))
        
    n = int(input())
