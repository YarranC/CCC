# Boiling Water

def main():
    B = int(input())

    P = 5 * B - 400

    print(P)

    if P < 100:
        print("1")

    elif P == 100:
        print("0")

    else:
        print("-1")

if __name__ == "__main__":
    main()
    
