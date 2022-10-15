#五、最大矩形
Lary = input().split(',')
Lmax = 0
for Mapy in range(len(Lary)):
    for Mapx in range(len(Lary[Mapy])):
        Lcount = 0
        for Ly in range(Mapy,len(Lary)):
            #print('Ly:',Ly)
            Lcount = 0
            Lbool=-1
            for Lx in range(Mapx,len(Lary[Mapy])):
                for Lrange_y in range(Mapy,Ly+1):
                    if (int(Lary[Lrange_y][Lx]) == 0):
                        Lbool = 0
                        Lcount = 0
                        break
                    #print('Lrange_y',Lrange_y)
                    Lcount += int(Lary[Lrange_y][Lx])                
                    #print('Mapy:',Mapy,'Mapx:',Mapx,'Ly:',Ly,'Lx:',Lx,'Lenx:',len(Lary[Mapy]),'Lrange_y:',Lrange_y,'Lcount:',Lcount)
                if (Lbool == 0):
                    break
                #print('Mapy:',Mapy,'Mapx:',Mapx,'Ly:',Ly,'Lcount:',Lcount)
                if (Lcount > Lmax): Lmax = Lcount
print(Lmax)