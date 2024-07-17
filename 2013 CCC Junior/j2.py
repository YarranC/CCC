# Rotating letters

letters = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

string = input()

for s in string:
    if not s in letters:
        print('NO')
        import sys
        sys.exit(0)

print('YES')
