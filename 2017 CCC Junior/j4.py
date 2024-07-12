# Favourite Times

D = int(input())
cycle = int(D/720)
D = D%720

if D < 34: 
    print(0+cycle*31) 
elif D < 71: # 1:11
    print(1+cycle*31)
elif D < 83: # 1:23
    print(2+cycle*31)
elif D < 95: # 1:35
    print(3+cycle*31)
elif D < 107: # 1:47
    print(4+cycle*31)
elif D < 119: # 1:59
    print(5+cycle*31)
elif D < 130: # 2:10
    print(6+cycle*31)
elif D < 142: # 2:22
    print(7+cycle*31)
elif D < 154: # 2:34
    print(8+cycle*31)
elif D < 166: # 2:46
    print(9+cycle*31)
elif D < 178: # 2:58
    print(10+cycle*31)
elif D < 201: # 3:21
    print(11+cycle*31)
elif D < 213: # 3:33
    print(12+cycle*31)
elif D < 225: # 3:45
    print(13+cycle*31)
elif D < 237: # 3:57
    print(14+cycle*31)
elif D < 260: # 4:20
    print(15+cycle*31)
elif D < 272: # 4:32
    print(16+cycle*31)
elif D < 284: # 4:44
    print(17+cycle*31)
elif D < 296: # 4:56
    print(18+cycle*31)
elif D < 331: # 5:31
    print(19+cycle*31)
elif D < 343: # 5:43
    print(20+cycle*31)
elif D < 355: # 5:55
    print(21+cycle*31)
elif D < 390: # 6:30
    print(22+cycle*31)
elif D < 402: # 6:42
    print(23+cycle*31)
elif D < 414: # 6:54
    print(24+cycle*31)
elif D < 461: # 7:41
    print(25+cycle*31)
elif D < 473: # 7:53
    print(26+cycle*31)
elif D < 520: # 8:40
    print(27+cycle*31)
elif D < 532: # 8:52
    print(28+cycle*31)
elif D < 591: # 9:51
    print(29+cycle*31)
elif D < 671: # 11:11
    print (30+cycle*31)
else: # 12:34
    print(31+cycle*31)
