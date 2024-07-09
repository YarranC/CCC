# Silent Akbar

def main():
    
    hb_name = ""
    hb_money = 0
    
    for x in range(int(input())):
        Name = input()
        Money = int(input())

        if Money > hb_money:
            hb_money = Money
            hb_name = Name

    print(hb_name)

if __name__ == "__main__":
    main()
