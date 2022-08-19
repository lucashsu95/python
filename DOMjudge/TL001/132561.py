#TL001 成對資料的次大值之和
data = sorted(input().split())
Lsum = 0
for i in range(0,len(data),2):
    if data[i] >= data[i+1]:
        Lsum += int(data[i+1])
    else:
        Lsum += int(data[i])


print(Lsum)