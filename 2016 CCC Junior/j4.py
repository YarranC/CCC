# Arrival Time

d = 240
s1= 2
s2= 1

def time(h, m):
    s = ''
    if h < 10:
        s = '0'
    s += str(h)
    s += ':'
    if m < 10:
        s += '0'
    s += str(m)
    print(s)
    
hh, mm = input().split(':')
hh = int(hh)
mm = int(mm)
h = hh
m = mm

if hh >= 5 and hh < 7:
    t = (7 - hh)*60 - mm
    d2 = d - s1*t
    t2 = d2/s2
    h = 7 + int(t2/60)
    if h == 10:
        m = int(t2%60/2)
    else:
        m = int(t2%60)
elif hh >= 7 and hh < 10:
    t = (10 - hh)*60 - mm
    d2 = d - s2*t
    t2 = d2/s1
    h = 10 + int(t2/60)
    m = int(t2%60)
elif hh >= 13 and hh < 15:
    t = (15 - hh)*60 - mm
    d2 = d - s1*t
    t2 = d2/s2
    h = 15 + int(t2/60)
    m = int(t2%60)
elif hh >= 15 and hh < 19:
    t = (19 - hh)*60 - mm
    d2 = d - s2*t
    t2 = d2/s1
    h = 19 + int(t2/60)
    m = int(t2%60)
else:
    h = hh + 2
    m = mm

time(h%24, m)
