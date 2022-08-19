#TA001 二維矩陣2
data = input().split()
line = len(data) // 3
ary = [[],[],[]]
j = 0
for i in range(len(data)):
    if i % line == 0 and i >= 1:
        j += 1
    ary[j].append(data[i])
    

# print(ary)
ary2 = [[] for i in range(line)]
for i in ary:
    for j in i:
        ary2[i.index(j)].append(j)

# print(ary2)
    
ans = []
for j in ary2:
    Lmax = 0
    Lmax2 = 0
    for k in j:
        if int(k) > Lmax2:
            Lmax2 = int(k)
        if Lmax2 > Lmax:
            Lmax,Lmax2 = Lmax2,Lmax
    ans.append(Lmax2)
output = []
for _ in range(3):
    output.append(ans)
print(output)


