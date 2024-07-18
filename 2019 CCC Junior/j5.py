# Rule of Three

rules = []

for i in range(3):
    rules.append(input().split())

S, I, F = input().split()
S = int(S)

W = []  # rule, start, result
memo = {}

def check(string, step):
    if (string, step) in memo:
        return memo[(string, step)]
    
    if step == S:
        result = 1 if string == F else 0
        memo[(string, step)] = result
        return result
    
    for r, rule in enumerate(rules):
        start = 0
        while True:
            i = string.find(rule[0], start)
            if i == -1:
                break
            
            result = string[:i] + rule[1] + string[i + len(rule[0]):]
            W.append([r + 1, i + 1, result])
            
            if check(result, step + 1) == 1:
                memo[(string, step)] = 1
                return 1
            
            W.pop()
            start = i + 1
    
    memo[(string, step)] = 0
    return 0

if check(I, 0) == 1:
    for w in W:
        print(*w, sep=" ")
