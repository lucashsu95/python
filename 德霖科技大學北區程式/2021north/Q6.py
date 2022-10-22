#試題六(16 分)：裂解之數
Lcount_ary = []
Lcount = 0
datas = list(map(int,input().split()))
for i in range(datas[0],datas[-1]+1):
    for j in range(2,i):
        t1 = j
        while t1 < i:
            t1 *= j

        # print(t1)
        if t1 == i:
            Lcount += 1
            break   
print(Lcount)
#13m