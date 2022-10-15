#1101 C票選動物
Ldict = {}
while 1:
    try:
        Linput = input()
        if Linput in Ldict.keys():
            Ldict[Linput] += 1
        else:
            Ldict[Linput] = 1
    except:
        break

for Lkey,Lvalue in zip(Ldict.keys(),Ldict.values()):
    if Lvalue == max(Ldict.values()):
        print(Lkey)