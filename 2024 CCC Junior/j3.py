# Bronze Count

def main():
    N = int(input()) # number of participant
    
    G = 0 # Score for gold
    Pg = 0 # how many participant achieved gold score
    
    S = 0 # Score for silver
    Ps = 0 # how many participant achieved silver score
    
    B = 0 # score required for bronze level
    Pb = 0 # how many participant achieved bronze score

    for x in range(N):
        x = int(input())
        if x > G:
            B = S
            Pb = Ps
            
            S = G
            Ps = Pg

            G = x
            Pg = 1
        elif x == G:
            Pg += 1
            
        elif x > S:
            B = S
            Pb = Ps

            S = x
            Ps = 1
        elif x == S:
            Ps += 1
        elif x > B:
            B = x
            Pb = 1
        elif x == B:
            Pb += 1
    
    print(B, Pb)

if __name__ == "__main__":
    main()
