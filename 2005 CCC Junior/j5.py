# Problem J5: Bananas

def check(word):
    if word == 'A':
        return True

    w = word
    i = 0
    while 'N' in w:
        i += w.index('N')
        if check(word[0:i]) and check(word[i+1:]):
            return True
        else:
            w = word[i+1:]
            i+=1           
        
    if len(word) > 2 and word[0] == 'B' and word[len(word)-1] == 'S' and check(word[1:len(word)-1]):   
        return True

    return False

word = input()
while word != 'X':
    if check(word):
        print('YES')
    else:
        print('NO')
    word = input()
