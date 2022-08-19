#TL001 字串間共同使用的字母
data = input().split()
data2 = list(set(data[0]))
Lans = []

for i in range(len(data2)):
    Lcount = -1
    for j in range(len(data)):
        if data[j].count(data2[i]) == 0:
            Lcount = -1
            break
        else:
            if (Lcount == -1):
                Lcount = data[j].count(data2[i])

            if (Lcount > data[j].count(data2[i])):
                Lcount = data[j].count(data2[i])
    if Lcount >0:
        for k in range(Lcount):
            Lans.append(data2[i])
Lans = "".join(sorted(Lans))
print(Lans)
