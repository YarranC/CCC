# Post's Correspondence Problem

m = int(input())
n = int(input())

A = []
B = []

for i in range(n):
    A.append(input())

for i in range(n):
    B.append(input())

seq = []

def check(set1, set2):

    seq1 = ''
    seq2 = ''
    for i in range(len(seq)):
        seq1+=set1[seq[i]-1]
        seq2+=set2[seq[i]-1]

    #print('check', seq1, seq2)
    return seq1 == seq2
    

def build(k):
    global A, B, n, m

    if k >= m:
        return check(A, B)

    for i in range(n):
        seq.append(i+1)
        #print(seq)
        #input()
        if check(A, B):
            return True
        
        if build(k + 1):
            return True
        else:
            seq.pop(len(seq)-1)

    return False

if build(0):
    print(len(seq))
    for i in range(len(seq)):
        print(seq[i])
else:
    print('No solution.')