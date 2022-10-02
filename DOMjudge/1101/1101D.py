#1101 D化學廢料
n = int(input())
datas = input().split()
Ldict = {}
for i in datas:
    if i in Ldict.keys():
        Ldict[i] += 1
    else:
        Ldict[i] = 1
print(len(Ldict))