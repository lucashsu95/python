while 1:
    try:
        n = int(input())
        if n == 0:
            break
        Lary = []
        data = input().split()
        Lset = set()
        while data != ['0']:
            for i in data:
                if i != data[0]:
                    Lary.append([i,data[0]])
                Lset.add(i)
            data = input().split()
        Lset = sorted(Lset)
        # print('Lset:',Lset)
        # print('Lary:',Lary)
        Lcount = 0
        for i in range(len(Lset)):
            time = 0
            Lary2 = Lary.copy()
            while time != len(Lary2):
                # print(Lary2[time],Lset[i])
                if Lary2[time][0] == Lset[i] or Lary2[time][1] == Lset[i]:
                    Lary2.pop(time)
                    time = 0
                else:
                    time += 1
            Lans = []
            # print('Lary2:',Lary2)

            Lary3 = []
            for i in Lary2:
                for j in i:
                    Lary3.append(j)
            # print(Lary3)

            Lbool = True
            for i in Lary3:
                Lcount2 = 0
                for j in Lary3:
                    if i == j:
                        Lcount2 += 1
                if Lcount2 > 1:
                    Lbool = False
            # print('Lbool:',Lbool)


            for i in Lary2:
                for j in i:
                    Lans.append(j)
            # print(set(Lans))

            if len(set(Lans)) != n-1 or Lbool:Lcount += 1
            # print('Lcount:',Lcount)
        print(Lcount)
    except:
        break
