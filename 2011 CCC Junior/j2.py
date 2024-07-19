# Who Has Seen The Wind

h = int(input())
M = int(input())

def altitude(h, t):
    return -6*pow(t, 4) + h*pow(t, 3) + 2*pow(t, 2) + t

t = 1

while t <= M:
    if altitude(h, t) <= 0:
        print("The balloon first touches ground at hour:")
        print(t)
        import sys
        sys.exit(0)
    t+=1
    
print("The balloon does not touch ground in the given time.")
