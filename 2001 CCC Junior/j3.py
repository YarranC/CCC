# Keeping Score

points = {'A' : 4, 'K' : 3, 'Q' : 2, 'J' : 1}
count = [0, 0, 0, 0]
suits = ['C', 'D', 'H', 'S']

def cnt(s):
    if count[s] == 0:
        return 3
    elif count[s] == 1:
        return 2
    elif count[s] == 2:
        return 1
    else:
        return 0
    
cards = input()
print('Cards Dealt Points')
s = 0
p = 0
total = 0
for i in range(17):
    c = cards[i]
    
    if c in suits:
        s = suits.index(c)

        match c:
           case 'C':
               print('Clubs', end=' ')
           case 'D':
               p+=cnt(0)
               print('   ', p)
               total+=p
               p = 0
               print('Diamonds', end=' ')
           case 'H':
               p+=cnt(1)
               print('   ', p)
               total+=p
               p = 0
               print('Hearts',  end=' ')
           case 'S':
               p+=cnt(2)
               print('   ', p)
               total+=p
               p = 0
               print('Spades',  end=' ')
    else:
        print(c, end=' ')
        if c in points:
            p+=points[c]
        count[s]+=1

p+=cnt(3)
total+=p
print(p)
print('     Total', total) 

