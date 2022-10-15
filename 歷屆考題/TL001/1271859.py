#TL001 重組句子中的單字
data = input().split()
ary = [[] for _ in range(len(data))]

for i in range(len(data)):
    
    ary[int(data[i][-1])-1].append(data[i][:-1])
ans = ''
for i in ary:
    for j in i :
        ans += j + ' '
print(ans)
