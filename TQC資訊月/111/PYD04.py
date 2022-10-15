n = 7
Lcount = 0
for i in range(1,n+1):
    star = (i+Lcount) * '*'
    Lcount += 1
    Lspace = ' ' * (n - i)
    print(Lspace + star)