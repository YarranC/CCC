# Problem J1: ISBN

digits = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]

for _ in range(3):
    digits.append(int(input()))

s = 0
for i in range(13):
    if i%2 == 0:
        s+=digits[i]*1
    else:
        s+=digits[i]*3

print("The 1-3-sum is", s)


