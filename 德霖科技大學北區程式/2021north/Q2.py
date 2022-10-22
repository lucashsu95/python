#試題二(16 分)：總流程時間
datas = list(map(int,input().split()))
datas = sorted(datas[:-1])
print(datas)
t1 = Lsum = 0
Lstr = ''
for i in range(len(datas)):
    t1 += datas[i]
    Lsum += t1
    Lstr += '+' + str(t1)
Lstr = Lstr[1:]
print(f"{Lsum}={Lstr}")
#6m