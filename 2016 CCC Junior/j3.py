# Hidden Palindrome

def check(s):
    if len(s) > 0:
        t = s.copy()
        t.reverse()
        return t == s
    else:
        return False

string = [x for x in input()]
length = 0

for x in range(len(string)):
    for y in range(len(string)-x):
        if check(string[x: len(string)-y]):
            length = max(length, len(string)-y-x)
print(length)
        

