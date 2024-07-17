# From 1987 to 2013
year = input()

def check(y):
    t = []
    for c in y:
        if not c in t:
            t.append(c)
        else:
            return True

    return False

d = 1
while check(str(int(year)+d)):
    d+=1

print(int(year)+d)
