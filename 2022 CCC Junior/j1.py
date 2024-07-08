## Cupcake Party

def main():
    r = int(input())
    s = int(input())

    output = (r * 8 + s * 3) - 28

    if output < 0:
        output = 0
        
    print(output)

if __name__ == "__main__":
    main()
    
