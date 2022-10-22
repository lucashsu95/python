while 1:
    try:

        Llist = [[],[],[],[]]
        datas = input().split()
        j = 0
        for i in range(1,len(datas)+1):
            Llist[j].append(datas[i-1])
            if i % 2 == 0 :
                j += 1
        center = []
        nocenter = []
        for i in range(len(Llist)):
            if Llist.count(Llist[i]) == 2:
                center.append(Llist[i])
            else:
                nocenter.append(Llist[i])
        # print(center)
        # print(nocenter)

        x4 = eval(nocenter[0][0] + '+' + nocenter[1][0] + '-' + center[0][0])
        y4 = eval(nocenter[0][1] + '+' + nocenter[1][1] + '-' + center[0][1])
        x4 = f"{x4:.3f}"
        y4 = f"{y4:.3f}"
        print(x4,y4)
    except:
        break