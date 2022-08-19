#104B樂透
Ln = int(input())
Lans = input().split(',')
for i in range(Ln):
    Lcut = Lcut2 = Lcut3 = Lcut4 = Lcut5 = 0
    Linput = input().split(',')
    Linput2 = []
    for j in range(0,6):
        Linput2.append([])
        for k in range(len(Linput)):
            Linput2[j].append(Linput[k])
        Linput2[j].remove(Linput[j])
    for p in Linput2:
        Lcut = 0
        for m in p:
            if m in Lans:
                Lcut += 1
            # print('m in Lans:',m,p)
            # print(Lcut)
        if Lcut == 5:Lcut5 += 1
        elif Lcut == 4:Lcut4 += 1
        elif Lcut == 3:Lcut3 += 1
        elif Lcut == 2:Lcut2 += 1
    print(f'{Lcut2},{Lcut3},{Lcut4},{Lcut5}')
    
