#TA001 二維矩陣
data = input().split()
line = int(len(data) ** 0.5)
ary = [[]]
j = 0
for i in range(len(data)):
    if i != 0 and i != 1 and i % line == 0:
        ary.append([])
        j += 1
    
    ary[j].append(data[i])

L_bool = True
for a in range(len(ary)):
    for b in range(len(ary)):
        if ary[a][b] != ary[b][a]:
            L_bool = False

if L_bool:
    print('True')
else:
    print('False')
