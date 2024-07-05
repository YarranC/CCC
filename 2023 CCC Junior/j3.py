# Special Event

def main():
    N=int(input()) # number of people interested in attending

    days = [0 for i in range(5)]

    # get availabilities
    for x in range(N):
        avail = input()
        
        for i, a in enumerate(avail):
            if avail[i] == 'Y':
                days[i]+=1

    # find maximum available days
    max_day = 0
    output = []
    for i in range(5):
        if days[i] > days[max_day]:
            max_day = i
            output = [max_day+1]
        elif days[i] == days[max_day]:
            output.append(i+1)

    # output the days  
    for i in range(len(output)-1):
        print(output[i], end=",")
    print(output[len(output)-1])

if __name__ == "__main__":
    main()
