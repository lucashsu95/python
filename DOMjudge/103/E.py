#103E撲克牌遊戲
Ln = int(input())
for i in range(Ln):
    Lnum = list(map(int, input().split()))
    Lnum.sort()

    Lcard = []
    for j in range(0,53):
        Lcard.append(0)

    for j in range(0,len(Lnum)):
        Lcard[Lnum[j]]=1

    #print(Lcard)
        
    Lorder = Lnum.copy()

    j = 0
    while j != len(Lorder):
        if Lorder[j] > 13:
            Lorder[j] = Lorder[j] % 13
            if Lorder[j] == 0:
                Lorder[j] = 13
        j += 1
    
    Lorder.sort()
    Lsingle = list(set(Lorder))
    #print(Lnum)
    Lpoint = 0
    if Lsingle[0]==1: Lsingle.append(14)
    #print(Lsingle)
    
    Lstart = 0
    
    for j in range(0,3):
        if j+4<len(Lsingle):
            if (Lsingle[j+1]-Lsingle[j]==1 and Lsingle[j+2]-Lsingle[j+1]==1 and Lsingle[j+3]-Lsingle[j+2]==1 and Lsingle[j+4]-Lsingle[j+3]==1 ):
                if Lpoint < 4: Lpoint = 4
                Lstart = j

                Lpos = Lsingle[Lstart]
                #print(Lpos)
                LcountB = 0
                for j in range(0,4):
                    if Lpoint ==4:
                        Lpos2 = Lpos+(j*13)
                        if Lcard[Lpos2] == 1:
                            #print(Lpos2)
                            for k in range(Lpos2,Lpos2+5):
                                Lmax=(Lpos2//13+1)*13
                                #print(Lmax)
                                if (k <= Lmax):
                                    if Lcard[k] == 1:
                                        LcountB +=1
                            if Lpos2 % 13 == 10:
                                if Lcard[Lpos2-9]==1:
                                    LcountB +=1
                            if LcountB == 5:
                                Lpoint = 7
                

    #print(Lpoint)
    if Lpoint == 0:
        LcountA = []
        for j in range(0,14):
            LcountA.append(0)

        for j in range(0,len(Lorder)):
            LcountA[Lorder[j]]+=1

        Lcount2 = 0
        Lcount3 = 0
        Lcount4 = 0
        for j in range(1,14):
            if (LcountA[j]>=4): Lcount4 = 1
            if (LcountA[j]==3): Lcount3 += 1
            if (LcountA[j]==2): Lcount2 += 1
        
        if (Lcount2>0): 
            Lpoint = Lcount2
            if Lpoint > 2:
                Lpoint = 2
        if (Lcount3>0): Lpoint = 3
        if (Lcount3>1): Lpoint = 5
        if (Lcount3>0 and Lcount2 >0): Lpoint = 5
        if (Lcount4>0): Lpoint = 6
        #print(LcountA)
    print(Lpoint)
            

    
