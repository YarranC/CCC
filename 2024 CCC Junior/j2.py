# Dusa And The Yobis

def main():
    D = int(input())
    while True:
        x = int(input())
        if D > x:
            D += x
        else:
            print(D)
            break

if __name__ == "__main__":
    main()
