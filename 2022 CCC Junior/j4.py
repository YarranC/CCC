## Good Groups
    
def main():
    # must rules
    must = dict()
    for _ in range(int(input())):
        key, val = input().split()
        if key not in must:
            must[key] = [val]
        else:
            must[key].append(val)    

    # must not rules
    mustnot = dict()
    for i in range(int(input())):
        key, val = input().split()
        if key not in mustnot:
            mustnot[key] = [val]
        else:
            mustnot[key].append(val)   
    
    # go through the groups
    viol = 0
    for _ in range(int(input())):
        g = set(input().split())
        for i in g:
            viol += sum(1 for m in must.get(i, []) if m not in g)
            viol += sum(1 for m in mustnot.get(i, []) if m in g)
    print(viol)
        
if __name__ == "__main__":
    main()
    
