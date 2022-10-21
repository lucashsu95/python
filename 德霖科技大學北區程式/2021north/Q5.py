#試題五(16 分)：物品探測
import sys

Larya = []
Laryb = []
Lroot = True
Lroot2 = True
ans1 = 0
ans2 = 0

for line in sys.stdin.read().splitlines():
    a,b = line.split(' ')
    Larya.append(a)
    Laryb.append(b)
for i in range(len(Larya)-1):
    if Larya[2] == Larya[i]:
        Lroot = False
        if i == 0:
            ans1 = Larya[1]
        else:
            ans1 = Larya[0]    
    if Laryb[2] == Laryb[i]:
        Lroot2 = False
        if i == 0:
            ans2 = Laryb[1]
        else:
            ans2 = Laryb[0]

if Lroot :
    ans1 = Larya[2]
if Lroot2:
    ans2 = Laryb[2]
print(ans1,ans2)

        
