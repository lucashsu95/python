#題目 8： 生成樹(Spanning Tree)問題 (15%) 
n = int(input())
Lnow_ary = []
while 1:
    try:
        data = input().split()

        Lnow_ary.append([int(data[2]),data[1],data[0]])
    except:
        break

Lnow_ary.sort()
Lresult_ary = [Lnow_ary[0]]
for i in range(1,len(Lnow_ary)):
    Lclon_ary = []
    Lbool = True
    # print('i:',i,Lresult_ary)
    for j in range(i):
        Lvalue = list(set([Lnow_ary[i][1],Lnow_ary[i][2],Lnow_ary[j][1],Lnow_ary[j][2]]))
        if Lvalue not in Lclon_ary:
            Lclon_ary.append(Lvalue)
        else:
            Lbool = False
            break
    if Lbool:
        Lresult_ary.append(Lnow_ary[i])

Lans = 0
for i in range(len(Lresult_ary)):
    Lans += Lresult_ary[i][0]
print(Lans)