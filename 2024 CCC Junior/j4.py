# Troublesome Keys

def main():
    right_key = '-'
    silly_key = '-'
    quiet_key = '-'

    correct_string = input()
    wrong_string = input()

    j = 0 # current correct string character position
    
    for i, cur_key in enumerate(correct_string):
        # if quiet key, doesn't need to check again
        if correct_string[i] != quiet_key: 
            # if silly key, doesn't need to check again
            if correct_string[i] == silly_key: 
                j+=1
            # if repeat key, go to the next one
            elif i+1 < len(correct_string) and correct_string[i] == correct_string[i+1]: 
                j+=1
            # if found the wrong key
            elif j < len(wrong_string) and cur_key != wrong_string[j]: 
                # check if next character is the same, if same, found the quiet key, if not, found the silly key
                if i+1 < len(correct_string) and correct_string[i+1] == wrong_string[j]:
                    quiet_key = correct_string[i]         
                else:
                    right_key = cur_key
                    silly_key = wrong_string[j]
                    j+=1
            # if the last character is the quiet key
            elif j == len(wrong_string): 
                quiet_key = correct_string[i]
            else:
                j+=1
    
    print(right_key, silly_key)
    print(quiet_key)

if __name__ == "__main__":
    main()
