#四、英文字母出現次數
Lstr = list(input().lower().replace(' ',''))[:-1]
LaryMax,Lans = [],[]
Lcount = 0
Lset = list(sorted(set(Lstr)))
for i in Lset:
    LaryMax.append(Lstr.count(i))

for i in range(5):
    Lcount += max(LaryMax)
    Lans.append(Lset[LaryMax.index(max(LaryMax))])
    Lset.pop(LaryMax.index(max(LaryMax)))
    LaryMax.pop(LaryMax.index(max(LaryMax)))

print(Lcount)
print(''.join(Lans))