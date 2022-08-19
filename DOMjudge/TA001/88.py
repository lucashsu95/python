#TA001 重複文字只保留一個
data = list(input())
data2 = data.copy()

for i in range(len(data)):
    if data.count(data[i]) >= 2:
        data[i] = []


for j in range(len(data)-1,0,-1):
    if data2.count(data2[j]) >= 2:
        data2[j] = []

while [] in data:
    data.remove([])
while [] in data2:
    data2.remove([])

ans = ''.join(data)
ans2 = ''.join(data2)
print(ans2)
print(ans)



