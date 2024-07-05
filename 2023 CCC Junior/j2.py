#Chili Peppers

def main():
    N=int(input())

    SHU = 0
    for x in range(N):
        P=input().lower()

        match P:
            case "poblano":
                SHU+=1500

            case "mirasol":
                SHU+=6000

            case "serrano":
                SHU+=15500

            case "cayenne":
                SHU+=40000

            case "thai":
                SHU+=75000

            case "habanero":
                SHU+=125000

            case _:
                print("This object is unavailable")
                return -1
 
    
    print(SHU)

if __name__ == "__main__":
    main()
    
