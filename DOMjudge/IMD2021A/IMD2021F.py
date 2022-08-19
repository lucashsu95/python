#IMD2021 prob-字串中是否純粹都是數字
x,y = input().split(' ')
if x.isdigit() and y.isdigit():
    print(eval(x+'-'+y))
else:
    print('NaN')
