# Magic Squares

ms = 0
column = [0 for _ in range(4)]

for row in range(4):
    s = 0
    c = 0
    for r in input().split():
        r = int(r)
        s += r
        column[c]+=r
        c += 1

    if row == 0:
        ms = s
    elif ms != s:
        print("not magic")
        import sys
        sys.exit(0)

for col in range(4):

    if column[col] != ms:
        print("not magic")
        import sys
        sys.exit(0)

print("magic")
