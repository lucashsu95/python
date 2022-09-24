#五、最大矩形
Lary = input().split(',')
Lxmax = Lymax = Lzmax = -1
for i in range(len(Lary)):
    for j in range(len(Lary[i])):
        Lxcount = Lycount = Lzcount = 0
    #x
        for x in range(j,len(Lary[i])):
            if Lary[i][x] == '0':
                break
            Lxcount += int(Lary[i][x])
            if Lxcount > Lxmax:
                Lxmax = Lxcount
    #y
        for y in range(len(Lary)):
            if Lary[y][j] == '0':
                break
            Lycount += int(Lary[y][j])
            if Lycount > Lymax:
                Lymax = Lycount
    #z
        for z in range(len(Lary)):
            Lbool = True
            if j+z == len(Lary[i]) or i+z == len(Lary) or i == len(Lary)-1 or j == len(Lary):
                break
            for k in range(i,i+z+1):
                if Lbool == False:
                    break
                for p in range(j,j+z+1):
                    if Lary[k][p] == '0':
                        Lbool = False
                        break

                    Lzcount += int(Lary[k][p])
                    # print(Lary[k][p])
            if Lzcount > Lzmax:
                Lzmax = Lzcount
            Lzcount = 0
            # print(i+z,j+z)
            # print('i,j,z:',i,j,z)
ans = [Lxmax,Lymax,Lzmax]
print(max(ans))
