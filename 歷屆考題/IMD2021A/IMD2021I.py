#IMD2021A 逆序數對
while 1:
    try:
        n = int(input())
        if n == 0:exit()
        ary = []
        Lcount = 0
        for i in range(n):ary.append(int(input()))

        for i in range(1,len(ary)):
            #print(ary[0:i])
            for j in ary[0:i]:
                if j > ary[i]:
                    Lcount += 1
        print(Lcount)
                
        
    except:
        break
