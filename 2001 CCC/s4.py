# Cookies

n = int(input())

cookies = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    cookies.append([x, y])

#print(cookies)

longest = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                #print(cookies[i], cookies[j], cookies[k])
                a = round(pow(pow(cookies[i][0]-cookies[j][0], 2) + pow(cookies[i][1]-cookies[j][1], 2), 0.5), 5)
                b = round(pow(pow(cookies[i][0]-cookies[k][0], 2) + pow(cookies[i][1]-cookies[k][1], 2), 0.5), 5)
                c = round(pow(pow(cookies[k][0]-cookies[j][0], 2) + pow(cookies[k][1]-cookies[j][1], 2), 0.5), 5)
                s = round((a + b + c) / 2, 5)
                r = 0
                if pow(a, 2) + pow(b, 2) > pow(c, 2) or pow(a, 2) + pow(c, 2) > pow(b, 2) or pow(c, 2) + pow(b, 2) > pow(a, 2):
                    r = round(max(a, b, c) / 2, 5)
                else:
                    d = round(4 * pow(s * (s - a) * (s - b) * (s - c), 0.5), 5)
                    if d != 0:
                        r = round(a * b * c / d, 5)

                if r > longest:
                    longest = r
                #print(a, b, c, s, d, r)

print(format(longest*2,'.2f'))


