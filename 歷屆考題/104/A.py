#104A電梯電費計算系統
Ln = int(input())
for i in range(Ln):
    Ln2 = int(input())
    Lstr = list(map(int,input().split(',')))
    Lmoney = 0
    for j in range(1,len(Lstr)):
        if Lstr[j-1] < Lstr[j]:
            Lmoney += (Lstr[j] - Lstr[j-1]) * 20
        else:
            Lmoney += (Lstr[j-1] - Lstr[j]) * 10
    print(Lmoney)