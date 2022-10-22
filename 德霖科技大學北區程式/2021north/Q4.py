#試題四(18 分)：算式檢查
n = int(input())
a,b = [],[]

for _ in range(n):
    Lroot = True
    Lcount = 0
    datas = input()
    for i in datas:
        if i == '(':
            Lcount +=1
        elif i == ')':
            Lcount -= 1
        elif i == '[':
            Lcount += 1
        elif i == ']':
            Lcount -= 1

        if Lcount < 0:
            Lbool = False
            break
    if Lcount == 0 :
        print('Valid')
    else:
        print('Try again')
#15m