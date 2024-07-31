# Problem J3: Smile with similes

n = int(input())
m = int(input())

adj = []
for _ in range(n):
    adj.append(input())

noun = []
for _ in range(m):
    noun.append(input())

for i in range(n):
    for j in range(m):
        print(adj[i], 'as', noun[j])
