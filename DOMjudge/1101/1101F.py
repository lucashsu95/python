#1101 F漢明距離
n = int(input())
for _ in range(n):
    Lstr = input()
    Lstr2 = input()
    Lcount = 0
    for i in range(len(Lstr)):
        if Lstr[i] != Lstr2[i]:
            Lcount += 1
    print(Lcount)
