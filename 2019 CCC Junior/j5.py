# Rule of Three

rules = []

for i in range(3):
    rules.append(input().split())

S, I, F = input().split()
S = int(S)

W = [] # rule, start, result

def check(string, r, step):
    if step == S and string == F:
        return 1
    elif step == S and string != F:
        return 0
    else:
        rule = rules[r]
        try: string.index(rule[0])
        except: return 0
        # replace old substring with new substring
        i = string.index(rule[0])
        while i < len(string):
            if i != 0:
                result = string[0:i]+rule[1]+string[i+len(rule[0]):]
            else:
                result = rule[1]+string[i+len(rule[0]):]
            W.append([r+1, i+1, result])
            for n in range(3):
                if check(result, n, step+1) == 1:
                   return 1
            W.pop(len(W)-1)
            try: string.index(rule[0], i+1)
            except: return 0
            i = string.index(rule[0], i+1)
        
for r in range(3):
    if check(I, r, 0) == 1:
        break

for w in W:
    print(*w, sep=" ")
