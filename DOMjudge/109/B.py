#109B打印機
for i in range(int(input())):
    n = input()
    a = ''
    b = ''
    for j in n:
        if j == "4":
            a += "3"
            b += "1"
        else:
            a += j
            if b != '':
                b += '0'
            

    print(a,b)
    