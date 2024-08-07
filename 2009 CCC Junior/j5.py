# Problem J5: Degrees of Separation

relation = {}

def friend(x, y):
    if relation.get(x) == None:
        relation[x] = [y]
    elif y not in relation[x]:
        relation[x].append(y)
        
    if relation.get(y) == None:
        relation[y] = [x]
    elif x not in relation[y]:
        relation[y].append(x)

def unfriend(x, y):
    if relation.get(x) != None and y in relation[x]:
        relation[x].remove(y)
    
    if relation.get(y) != None and x in relation[y]:
        relation[y].remove(x)

def count_friend(x):
    if relation.get(x) != None:
        print(len(relation[x]))
    else:
        print(0)

def count_f_of_f(x):
    if relation.get(x) != None:
        count = 0
        frd = []
        for f in relation[x]:
            if relation.get(f) != None:
                for ff in relation[f]:
                    if ff != x and ff not in relation[x] and ff not in frd:
                        frd.append(ff)
                        count+=1
        print(count)
    else:
        print(0)

result = []
def degree_of_sep(x, y, fl):
    fl.append(x)
    degree = 50
    if relation.get(x) != None:
        if y in relation[x]:

            result.append(fl.copy())
            return 1
        for f in relation[x]:
            if f not in fl:
                d = degree_of_sep(f, y, fl)
                fl.remove(f)
                degree = min(degree, d)

    return degree + 1

    
friend(2, 6)
friend(1, 6)
friend(3, 6)
friend(4, 6)
friend(3, 4)
friend(4, 5)
friend(3, 5)
friend(5, 6)
friend(6, 7)
friend(7, 8)
friend(8, 9)
friend(9, 12)
friend(9, 10)
friend(10, 11)
friend(11, 12)
friend(3, 15)
friend(15, 13)
friend(12, 13)
friend(13, 14)
friend(16, 18)
friend(18, 17)
friend(16, 17)

cmd = input()

while cmd != 'q':
    match cmd:
        case 'i':
            friend(int(input()), int(input()))
        case 'd':
            unfriend(int(input()), int(input()))
        case 'n':
            count_friend(int(input()))
        case 'f':
            count_f_of_f(int(input()))
        case 's':
            degree = degree_of_sep(int(input()), int(input()), [])
            if degree == 51:
                print('Not connected')
            else:
                print(degree)

    cmd = input()
    

        
