#五、最大矩形
Lary = input().split(',')
Lxmax = Lymax = Lzmax = -1
Lmax = 0
for Mapy in range(len(Lary)):
    for Mapx in range(len(Lary[Mapy])):
        Lxcount = Lycount = Lzcount = 0
    #x

        for Ly in range(Mapy,len(Lary)):
            #print('Ly:',Ly)
            Lxcount = 0
            Lbool=-1
            for Lx in range(Mapx,len(Lary[Mapy])):
                for Lrange_y in range(Mapy,Ly+1):
                    if (int(Lary[Lrange_y][Lx]) == 0):
                        Lbool = 0
                        Lxcount = 0
                        break
                    #print('Lrange_y',Lrange_y)
                    Lxcount += int(Lary[Lrange_y][Lx])                
                    print('Mapy:',Mapy,'Mapx:',Mapx,'Ly:',Ly,'Lx:',Lx,'Lenx:',len(Lary[Mapy]),'Lrange_y:',Lrange_y,'Lxcount:',Lxcount)
                if (Lbool == 0):
                    break
                print('Mapy:',Mapy,'Mapx:',Mapx,'Ly:',Ly,'Lxcount:',Lxcount)
                if (Lxcount > Lmax): Lmax = Lxcount
print('max:',Lmax)

        

        # for x in range(j,len(Lary[i])):
        #     Lxcount += int(Lary[i][x])
        #     for xs in range(i,len(Lary)):
        #         Lxcount += int(Lary[xs][x])
        #     print(i,j,x)
        #     print(Lxcount)
        #     Lxcount = 0
        # print()
        
#     #y
#         for y in range(i,len(Lary)):
#             if Lary[y][j] == '0':
#                 break
#             Lycount += int(Lary[y][j])
#             if Lycount > Lymax:
#                 Lymax = Lycount
#     #z
#         for z in range(len(Lary)):
#             Lbool = True            
#             Lzcount = 0
#             for k in range(i,i+z):
#                 if Lbool ==False:
#                     break
#                 for p in range(j,j+z):
#                     if k >= len(Lary) or p >= len(Lary[i]) or Lary[k][p] == '0':
#                         Lzcount = 0
#                         Lbool = False
#                         break
#                     Lzcount += int(Lary[k][p])
#             if Lzcount > Lzmax:
#                 Lzmax = Lzcount
# ans = [Lxmax,Lymax,Lzmax]
# print(max(ans))
# print(ans)