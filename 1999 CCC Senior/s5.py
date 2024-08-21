# Letter Arithmetic - 
# for these 4 CCC test cases, only got the answer for the 2nd/4th cases
# BBXXXFFCXL
# BXJIULXSUQ
# ULQSCLLLQI
# 1155500756
# 1534265928
# 2689766684
#
# YOQFUQXTTXYOQFUQXTTX
# YQQUOXXUOTYQQUOXXUOT
# LYTQFIYLDYLYTQFIYLDY
# 12807856651280785665
# 18872557261887255726
# 31680413913168041391

word = ['', '', '']
letters = []
memo = {}

def get(w, p, n):
    global letters
    
    l = word[w][len(word[w]) - p]

    for i in range(10):
        if letters[i] == l:
            return i
    if letters[n] == '':
        letters[n] = str(l)
        return n
    return -1
        
    
def assign(pos, carry):
    global letters, memo

    # save a copy in case the assignment did not work
    temp = {}
    for k in letters.keys():
        temp[k] = letters[k]
    memo = {}
    
    for i in range(10):
        for j in range(10):
            for k in range(10):
                a = get(0, pos, i)
                b = get(1, pos, j)
                c = get(2, pos, k)

                if a >= 0 and b >= 0 and c >= 0 and memo.get((a, b, c)) == None:
                    s = a + b + carry - c
                    if s%10 == 0:
                        if pos == len(word[1]):
                            if s == 0 and c > 0:
                                for w in range(3):
                                    for p in range(len(word[w])):
                                        print(get(w, len(word[w]) - p, 0), end='')   
                                    print()
                                print()
                                return True
                        elif assign(pos+1, s//10):
                            return True
                    
                if memo.get((a, b, c)) == None:
                    memo[(a, b, c)] = False    
                letters = {}
                for n in temp.keys():
                    letters[n] = temp[n]

    return False
                        
                    
    
for _ in range(int(input())):
    word[0] = input()
    word[1] = input()
    word[2] = input()

    # letter of corresponding digit 0, 1, 2...., 9
    letters = {i : '' for i in range(10)}

    # assign each letter a digit, starting from rightmost   
    assign(1, 0)
