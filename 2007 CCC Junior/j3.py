# Deal or No Deal Calculator

dollar = {1 : 100, 2 : 500, 3 : 1000, 4 : 5000, 5: 10000, 6 : 25000, 7 : 50000, 8 : 100000, 9 : 500000, 10 : 1000000}

briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for _ in range(int(input())):
    briefcases.remove(int(input()))

offer = int(input())

total = 0
l = len(briefcases)

for i in briefcases:
    total+=dollar[i]

if total/l < offer:
    print('deal')
else:
    print('no deal')
