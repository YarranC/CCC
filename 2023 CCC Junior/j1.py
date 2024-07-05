# Deliv-e-droid

def main():
    p=int(input())
    c=int(input())

    output = 0

    output += 50*p
    output -= 10*c
    
    if p > c:
        output += 500
        
    print(output)
    
if __name__ == "__main__":
    main()

