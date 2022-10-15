Lstr = list(map(int,input().split()))
Lstr2 = Lstr.copy()
for i in range(1,len(Lstr)):
    if Lstr2[i-1] > Lstr2[i]:
        Lstr.remove(Lstr[i])
# print(Lstr)
print(len(Lstr))