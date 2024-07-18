# Big Bang Secrets

K = int(input())
string = input()

output = ''
p = 1
for c in string:
    s = ord(c) - 3*p - K
    if s < 65:
        output+=chr(s+26)
    else:
        output+=chr(s)
    p+=1

print(output)
