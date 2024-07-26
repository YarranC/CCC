# Problem J2 - AmeriCanadian

vowel = ['a', 'e', 'i', 'o', 'u', 'y']

word = input()
while word != 'quit!':
    if len(word) > 4 and word[len(word)-3] not in vowel and word[len(word) - 2:] == 'or':
        word = word[:len(word)-2]+'our'

    print(word)
    
    word = input()
