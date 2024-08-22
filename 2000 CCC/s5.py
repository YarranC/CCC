# sheep and coyotes

sheep = []
eaten = []

for _ in range(int(input())):
    sheep.append([float(input()), float(input())])

for i in range(len(sheep)):
    left, right = 0, 1000
    
    for j in range(len(sheep)):
        if i not in eaten and j not in eaten and i != j and sheep[j][1] != sheep[i][1]:
            x = (sheep[i][0] + sheep[j][0]) / 2
            y = (sheep[i][1] + sheep[j][1]) / 2
            s = (sheep[i][0] - sheep[j][0]) / (sheep[j][1] - sheep[i][1])
            if s == 0:
                if sheep[i][1] < sheep[j][1]:
                    eaten.append(j)
                else:
                    eaten.append(i)
            else:
                p = -y / s + x
                if sheep[j][0] < sheep[i][0]:
                    left = max(p, left)
                else:
                    right = min(p, right)

    if left >= right:
        eaten.append(i)

for j in range(len(sheep)):
    if j not in eaten:
        print('The sheep at (', format(sheep[j][0],'.2f'), ', ', format(sheep[j][1],'.2f'), ') might be eaten.', sep='')
