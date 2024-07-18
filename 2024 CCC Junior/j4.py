# Troublesome Keys

right_key = '-'
silly_key = '-'
quiet_key = '-'

correct_string = input()+'*'
wrong_string = input()+'*'

keys = [chr(i) for i in range(97, 123)]
for k in keys:
    if k in wrong_string and not k in correct_string:
        silly_key = k
        
j = 0 
    
for i in range(len(correct_string)):
    cur_key = correct_string[i]
    if cur_key == wrong_string[j]:
        j+=1
    elif wrong_string[j] == silly_key:
        right_key = cur_key
        j+=1
    else:
        quiet_key = cur_key

print(right_key, silly_key)
print(quiet_key)

