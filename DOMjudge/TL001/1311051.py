#TL001 排錯順序的數字個數
data = input().split()
ans = sorted(data)
Lcount = 0
for i,j in zip(data,ans):
    if i != j:
        Lcount += 1
print(Lcount)