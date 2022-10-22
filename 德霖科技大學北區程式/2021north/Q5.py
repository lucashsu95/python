#試題五(16 分)：物品探測
x_y = []
for _ in range(3):
    datas = input().split()
    x_y.append([int(datas[0]),int(datas[1])])
x_y.sort()
# print(x_y)
ansx = x_y[1][0] + x_y[2][0] - x_y[0][0] 
ansy = x_y[1][1] + x_y[2][1] - x_y[0][1]
print(ansx,ansy)
#6m