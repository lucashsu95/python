xy_ary = []
for i in range(5):
    datas = input().split(',')
    xy_ary.append([datas[0],datas[1]])
# print(xy_ary)
Lmax = 0
x_y = ''
for xy in xy_ary:
    for xy2 in xy_ary:
        Lrange = ((abs(int(xy[0]) - int(xy2[0]))) ** 2 + (abs(int(xy[1]) - int(xy2[1]))) ** 2) ** 0.5
        if Lrange > Lmax and xy != xy2:
            x_y = xy + xy2
            Lmax = Lrange
            # print(x_y)
            # print("Lmax:",Lmax)
print(Lmax/2)
x = (int(x_y[0])+int(x_y[2]))/2
y = (int(x_y[1])+int(x_y[3]))/2
print('圓心:',x,y)

