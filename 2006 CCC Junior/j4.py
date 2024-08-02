# It’s tough being a teen!

level=[[],[],[],[],[],[],[]]
tasks = {}
memo = [0, 0, 0, 0, 0, 0, 0]

# task : [level, [next tasks]]

def update(task):
    global tasks

    if tasks.get(task) == None:
        return
    
    lvl, n_tasks = tasks[task]
    level[lvl].remove(task)
    lvl+=1
    tasks[task][0] = lvl
    level[lvl].append(task)

    for t in n_tasks:
        update(t)


# check if t2 need to be done after t1
def is_n_task(t1, t2):
    global tasks
    
    if tasks.get(t1) == None:
        return False

    if t2 in tasks[t1][1]:
        return True

    for t in tasks[t1][1]:
        if is_n_task(t, t2):
            return True

    return False

def add_task(t1, t2):
    global tasks

    memo[t1-1] = 1
    memo[t2-1] = 1
    
    if tasks.get(t1) == None:
        tasks[t1] = [0, [t2]]
        level[0].append(t1)
    elif is_n_task(t2, t1):
        return False
    else:
        tasks[t1][1].append(t2)
    
    if tasks.get(t2) == None:
        tasks[t2] = [tasks[t1][0]+1, []]
        level[tasks[t1][0]+1].append(t2)

    while tasks[t2][0] <= tasks[t1][0]:
        update(t2)

    return True

add_task(1, 7)
add_task(1, 4)
add_task(2, 1)
add_task(3, 4)
add_task(3, 5)

t1 = int(input())
t2 = int(input())

while t1 != 0 and t2 != 0:
    if not add_task(t1, t2):
        print('Cannot complete these tasks. Going to bed.')
        import sys
        sys.exit(0)
    
    t1 = int(input())
    t2 = int(input())

for i in range(7):
    level[i].sort(reverse=True)

todo = []

def sort(task):
    global todo

    if todo == []:
        todo.append(task)
        return

    i = 0
    f = False
    for t in todo:
        if is_n_task(t, task):
            i = todo.index(t)+1
        elif task < t and not f:
            i = min(i, todo.index(t))
            f = True
        elif task > t and not f:
            i = todo.index(t)+1

    todo.insert(i, task)

for i in range(7):
    for j in range(len(level[i])):
        sort(level[i][j])

for i in range(7):
    if memo[i] == 0:
        sort(i+1)
        
print(*todo)
