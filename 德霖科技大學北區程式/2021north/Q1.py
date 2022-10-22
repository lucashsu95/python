#試題一(18 分)：連分數轉換
datas = sorted(list(map(int,input().split(','))),reverse=True)
t = f"{datas[0]}/{1}"
# print(t)
for i in range(1,len(datas)):
    # print(datas[i])
    t1,t2 = list(t.split('/'))

    t = f"{int(t2)+int(t1)*datas[i]}/{t1}"
    # print(t)
print(t)
#10m