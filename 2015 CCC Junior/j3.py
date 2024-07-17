#  Rovarspraket

vowel = [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]

string = input()

result = ''
for c in string:
    index = ord(c)
    result += c
    if not index in vowel:
        if index <= (vowel[0] + vowel[1])/2:
            result += 'a'
        elif index > (vowel[0] + vowel[1])/2 and index <= (vowel[1] + vowel[2])/2:
            result += 'e'
        elif index > (vowel[1] + vowel[2])/2 and index <= (vowel[2] + vowel[3])/2:
            result += 'i'
        elif index > (vowel[2] + vowel[3])/2 and index <= (vowel[3] + vowel[4])/2:
            result += 'o'
        else:
            result += 'u'
            
        if c == 'z':
            result += 'z'
        elif not ord(c)+1 in vowel: 
            result += chr(ord(c)+1)
        else:
            result += chr(ord(c)+2)
print(result)
            
