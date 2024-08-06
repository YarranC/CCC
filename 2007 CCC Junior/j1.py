# Who is in the middle?

a = int(input())
b = int(input())
c = int(input())

papa = max(a, b, c)
baby = min(a, b, c)

for i in [a, b, c]:
    if i != papa and i != baby:
        print(i)
