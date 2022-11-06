#題目 6：阿姆斯壯數(Armstrong number)問題 (15%)
Lstart,Lend = list(map(int,input().split(',')))
def fun(Lnum):
    #print("num:",Lnum)
    Lnum = list(str(Lnum))
    Lresult = 0
    for i in Lnum:
        Lresult += int(i)**len(Lnum)
    #print("result:",Lresult)
    return Lresult
Lans = []
for i in range(Lstart+1,Lend):
    if i == fun(i):
        Lans.append(str(i))
if Lans != []:
    print(','.join(Lans))
else:
    print('無')