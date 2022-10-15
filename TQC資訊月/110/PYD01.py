#一、距離判斷
Lx = int(input())
Ly = int(input())
LxSum = (Lx - 5)**2
LySum = (Ly - 6)**2

Lans = int((LxSum + LySum) ** 0.5)
if Lans <= 15:
    print('Inside')
else:
    print('Outside')