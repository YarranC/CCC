## Harp Tuning
def main():
    inst = input()

    string = ''
    num = 0

    for i in range(len(inst)):
        if inst[i] == '+':
            print(" tighten", end = " ")
            string = ''
        elif inst[i] == '-':
            print(" loosen", end = " ")
            string = ''
        elif inst[i].isdigit():
            print(inst[i], end = '')
            num = 1
        elif num == 1:
            print()
            num = 0
            print(inst[i], end = '')
        else:
            print(inst[i], end = '')

if __name__ == "__main__":
    main()
    
