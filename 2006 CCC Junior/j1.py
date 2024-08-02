# The New CCC (Canadian Calorie Counting)

burger = {1:461, 2:431, 3:420, 4:0}
drinks = {1:130, 2:160, 3:118, 4:0}
sides = {1:100, 2:57, 3:70, 4:0}
dessert = {1:167, 2:266, 3:75, 4:0}

total = burger[int(input())] + sides[int(input())] + drinks[int(input())] + dessert[int(input())]

print('Your total calorie count is ', total, '.', sep='')
