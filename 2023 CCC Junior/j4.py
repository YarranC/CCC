# Trianglane

def main():
    C = int(input()) # number of columns

    # get tile conditions
    tile = [[] for i in range(2)]
    
    for i in range(2):
        tile[i] = input().split()

    # calculate the length of the tape
    tape = 0
    for i in range(2):
        for j in range(C):
            if tile[i][j] == '1':
                tape+=3
                # check left and right neighbors
                if j > 0 and j < C and tile[i][j-1] == '1':
                    tape-=1
                if j >=0 and j < C-1 and tile[i][j+1] == '1':
                    tape-=1
                #check top and bottom neighbors    
                if i == 0 and j%2 == 0 and tile[i+1][j] == '1':
                    tape-=1
                elif i == 1 and j%2 == 0 and tile[i-1][j] == '1':
                    tape-=1
    
    print(tape)

if __name__ == "__main__":
    main()
    
