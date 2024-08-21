# Year 2000

month =  ['January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']

def check_date(year, mm, dd):               
    if dd < 1 or dd > 31:
        return False
    
    if mm in month:
        match mm:
            case 'January' | 'March' | 'May' | 'July' | 'August' | 'October' | 'December':
                if dd > 31:
                    return False
            case 'February':
                if year > 24:
                    year += 1900
                elif year < 25 and year >= 0:
                    year += 2000
                    
                if year%4 == 0 and dd > 29:
                    return False
                elif year%4 != 0 and dd > 28:
                    return False
            case 'April' | 'June' | 'September' | 'November':
                if dd > 30:
                    return False
            case _:
                return False

    elif mm.isdigit():
        mm = int(mm)
        if mm <= 0 or mm > 12:
            return False
        else:
           match mm:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                if dd > 31:
                    return False
            case 2:
                if year > 24:
                    year += 1900
                elif year < 25 and year >= 0:
                    year += 2000
                    
                if year%4 == 0 and dd > 29:
                    return False
                elif year%4 != 0 and dd > 28:
                    return False
            case 4 | 6 | 9 | 11:
                if dd > 30:
                    return False
            case _:
                return False
    else:
        return False

    return True
                
           
for _ in range(int(input())):
    line = input()

    # check month dd, yy
    i = 0
    while i < len(line):
        year, month, day = ['0', '', '0']
        # find the ',' char in line
        try:
            idx = i + line[i:].index(',')
        except:
            break
        #print(i, idx)
        valid = True

        # get the year
        if idx + 3 < len(line) and line[idx + 1] == ' ' and line[idx + 2:idx + 4].isdigit():
            year = line[idx+2:idx+4]
            #print('year', year)
        else:
            valid = False
            
        # get the day
        if valid and idx - 2 > 0 and line[idx-2: idx].isdigit():
            day = line[idx-2: idx]
            #print('day', day)
        else:
            valid = False
            
        # get the month
        if valid and idx - 6 >= 0 and line[idx-3] == ' ':
            c = idx - 4
            month = ''
            while c >= 0 and line[c] != ' ':
                month = line[c] + month
                c-=1
            #print('month', month)
        else:
            valid = False

        if valid and check_date(int(year), month, int(day)) == True:
            #print(year, month, day)
            yy = int(year)
            if yy > 24:
                year = '19' + year
            elif yy < 25 and yy >= 0:
                year = '20' + year
            line = line[:idx+2] + year + line[idx+4:]

        i = idx + 4
        

    # check dd/mm/yy
    i = 0
    while i < len(line):
        year, mm, dd = ['0', '', '0']
        # find the '/' char in line
        try:
            idx = i + line[i:].index('/')
        except:
            break
        #print(i, idx)
        valid = True

        # get the day
        if idx - 2 >= 0 and line[idx-2:idx].isdigit():
            if (idx - 3 >= 0 and line[idx-3] == ' ') or idx - 2 == 0:
                dd = line[idx-2:idx]
            else:
                valid = False
        else:
            valid = False

        # get the month
        if valid and idx + 2 < len(line) and line[idx+1:idx+3].isdigit():
            mm = line[idx+1:idx+3]
        else:
            valid = False

        # get the year
        if valid and idx + 5 < len(line) and line[idx+3] == '/' and line[idx+4:idx+6].isdigit():
            if (idx + 6 < len(line) and not line[idx+6].isalnum()) or idx + 5 == len(line) - 1:
                year = line[idx+4:idx+6]
            else:
                valid = False
        else:
            valid = False
           
        if valid and check_date(int(year), mm, int(dd)) == True:
            yy = int(year)
            if yy > 24:
                year = '19' + year
            elif yy < 25 and yy >= 0:
                year = '20' + year
            line = line[:idx+4] + year + line[idx+6:]

        i = idx + 6

    # check yy.mm.dd
    i = 0
    while i < len(line):
        year, mm, dd = ['0', '', '0']
        # find the '.' char in line
        try:
            idx = i + line[i:].index('.')
        except:
            break
        #print(i, idx)
        valid = True

        # get the year
        if idx - 2 >= 0 and line[idx-2:idx].isdigit():
            if (idx - 3 >= 0 and line[idx-3] == ' ') or idx - 2 == 0:
                year = line[idx-2:idx]
            else:
                valid = False
        else:
            valid = False

        # get the month
        if valid and idx + 2 < len(line) and line[idx+1:idx+3].isdigit():
            mm = line[idx+1:idx+3]
        else:
            valid = False

        # get the day
        if valid and idx + 5 < len(line) and line[idx+3] == '.' and line[idx+4:idx+6].isdigit():
            if (idx + 6 < len(line) and not line[idx+6].isalnum()) or idx + 5 == len(line) - 1:
                dd = line[idx+4:idx+6]
            else:
                valid = False
        else:
            valid = False
           
        if valid and check_date(int(year), mm, int(dd)) == True:
            yy = int(year)
            if yy > 24:
                year = '19' + year
            elif yy < 25 and yy >= 0:
                year = '20' + year
            line = line[:idx-2] + year + line[idx:]

        i = idx + 6
        
    print(line)       
