#TL001 右邊的最大值
data =list(map(int,input().split()))
ans = []
for i in range(len(data)):
    if data[i] == data[-1]:ans.append(-1)
    else:ans.append(max(data[i+1:]))
print(ans)

    