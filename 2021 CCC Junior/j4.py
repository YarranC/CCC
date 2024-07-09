# Arranging Books

# A function to count the number of books
def count(books) -> list:
    c = [0, 0, 0]
    for b in books:
        if b == 'L':
            c[0] += 1
        elif b == 'M':
            c[1] += 1
        else:
            c[2] += 1
    return c

def main():
    books = input()

    total = count(books)

    L_sec = count(books[0:total[0]])
    M_sec = count(books[total[0]:total[0]+total[1]])
    S_sec = count(books[total[0]+total[1]:])
    
    swap = 0
    # L[1] <-> M[0]
    if L_sec[1] == M_sec[0]:
        swap += L_sec[1]
        L_sec[1] = 0
        M_sec[0] = 0
    elif L_sec[1] > M_sec[0]:
        swap += M_sec[0]
        L_sec[1] -= M_sec[0]
        M_sec[0] = 0
    else:
        swap += L_sec[1]
        M_sec[0] -= L_sec[1]
        L_sec[1] = 0
        
    # M[2] <-> S[1]
    if M_sec[2] == S_sec[1]:
        swap += S_sec[1]
        M_sec[2] = 0
        S_sec[1] = 0
    elif M_sec[2] > S_sec[1]:
        swap += S_sec[1]
        M_sec[2] -= S_sec[1]
        S_sec[1] = 0
    else:
        swap += M_sec[2]
        S_sec[1] -= M_sec[2]
        M_sec[2] = 0

    # S[0] <-> L[2]
    if L_sec[2] == S_sec[0]:
        swap += L_sec[2]
        L_sec[2] = 0
        S_sec[0] = 0
    elif L_sec[2] > S_sec[0]:
        swap += S_sec[0]
        L_sec[2] -= S_sec[0]
        S_sec[0] = 0
    else:
        swap += L_sec[2]
        S_sec[0] -= L_sec[2]
        L_sec[2] = 0

    # should only need to do L[1] <-> M[2], M[2] <-> S[0]
    # and L[2] <-> S[1], S[1] <-> M[0]
    swap += L_sec[1]*2
    swap += L_sec[2]*2
        
    print(swap)

if __name__ == "__main__":
    main()
