# Problem J4/S2 - Poetry

vowel = ['a', 'e', 'i', 'o', 'u']

N = int(input())

for _ in range(N):
    line = []
    rhyme = ['', '', '', '']
    for i in range(4):
        line.append(input().split())
        line[i] = line[i][len(line[i])-1]
        line[i] = line[i].lower()
        
        s = ''
        for j in range(len(line[i])):
            if line[i][j] in vowel:
                s=line[i][j]
            else:
                s+=line[i][j]
                    
        if s == '' :
            s = line[i]
        rhyme[i] = s

    if rhyme[0] == rhyme[1] == rhyme[2] == rhyme[3]:
        print('perfect')
    elif rhyme[0] == rhyme[1] and rhyme[2] == rhyme[3]:
        print('even')
    elif rhyme[0] == rhyme[2] and rhyme[1] == rhyme[3]:
        print('cross')
    elif rhyme[0] == rhyme[3] and rhyme[1] == rhyme[2]:
        print('shell')
    else:
        print('free')


