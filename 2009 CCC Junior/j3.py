# Problem J3: Good times

ottawa = int(input())
print(ottawa, 'in Ottawa')

def convert(time, lag):
    new = time+lag
    if new >= 2400:
        new-=2400
    elif new < 0:
        new+=2400
    if new%100 > 60:
        new-=60
        new+=100
    return new

print(convert(ottawa, -300), 'in Victoria')
print(convert(ottawa, -200), 'in Edmonton')
print(convert(ottawa, -100), 'in Winnipeg')
print(convert(ottawa, 0), 'in Toronto')
print(convert(ottawa, 100), 'in Halifax')
print(convert(ottawa, 130), 'in St. John\'s')

