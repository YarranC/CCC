# https://dmoj.ca/problem/mccc3j1
# Mock CCC '22 Contest 1 J1 - Square Root Decomposition


N = int(input())
i = int(input())
j = int(input())
a = N - i**2
b = N - j **2
if abs(a)<abs(b):
    print(1)
else:
    print(2)
