#TL001 出現次數是否都不同
data = input().split()
data2 = list(set(data))
ary = []

for i in range(len(data2)):
    ary.append(data.count(data2[i]))
a = False
for i in range(len(ary)):
    if ary[0] != ary[i]:
        a = True            
        break
print(a)

