#TL001 交錯合併字串
data1 = input()
data2 = input()
Lstr = ''
if len(data1) > len(data2):
    data1,data2 = data2,data1
    for i in range(len(data1)):
        Lstr += data2[i]
        Lstr += data1[i]
else:
    for i in range(len(data1)):
        Lstr += data1[i]
        Lstr += data2[i]

Lstr += data2[len(data1):]
print(Lstr)