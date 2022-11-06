#題目 2：編碼問題 (15%)
datas = input().split(', ')
Loption_ary = []
Lnum_ary = []
for i in range(len(datas)):
    Loption,Lnum = datas[i].split()
    Loption_ary.append(Loption)
    Lnum_ary.append(int(Lnum))

LnumSort_ary = sorted(Lnum_ary)

Lary = []
i = 0
while 1:
    Lary.append([LnumSort_ary[i],LnumSort_ary[i] + LnumSort_ary[i+1],0])
    Lary.append([LnumSort_ary[i+1],LnumSort_ary[i] + LnumSort_ary[i+1],1])
    LnumSort_ary.insert(i+2,LnumSort_ary[i] + LnumSort_ary[i+1])
    i += 2
    if sorted(LnumSort_ary) != LnumSort_ary:
        LnumSort_ary.sort()
    if i+2 > len(LnumSort_ary):
        break
# print(datas)
# print(Loption_ary)
# print(Lnum_ary)
# print(LnumSort_ary)
# print(Lary)

Lend = LnumSort_ary[-1]
def rec(Lfather,Lstr,Ltitle):
    if Lend == Lfather:
        print(Ltitle+'  '+Lstr[::-1])
    for i in range(len(Lary)):
        if Lary[i][0] == Lfather:
            # print(Lary[i][1],Lstr)
            rec(Lary[i][1],Lstr+str(Lary[i][2]),Ltitle)

for i in range(len(Loption_ary)):
    rec(Lnum_ary[i],'',Loption_ary[i])