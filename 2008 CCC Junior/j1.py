# Problem J1: Body Mass Index

weight = eval(input())
height = eval(input())

BMI = weight/(pow(height, 2))

if BMI > 25:
    print('Overweight')
elif BMI >= 18.5 and BMI <= 25:
    print('Normal weight')
else:
    print('Underweight')
