# Deficient, Perfect, and Abundant

for _ in range(int(input())):
     num = int(input())
     fac = [1]
     for i in range(2, num):
         if i not in fac and num%i == 0:
             fac.append(i)
             if num//i not in fac: fac.append(num//i)

     s = 0
     for i in fac: s+=i
     if s < num:
         print(num, 'is a deficient number.')
     elif s == num:
         print(num, 'is a perfect number.')
     else:
         print(num, 'is an abundant number.')
