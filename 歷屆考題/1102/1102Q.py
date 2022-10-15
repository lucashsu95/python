n = int(input())
data = list(map(int,input().split()))
data.sort()
ans = []

for i in range(len(data)):
    Lsum = data[0] + data[1]
    ans.append(Lsum)
    del data[0]
    del data[0]
    data.append(Lsum)
    data.sort()
    if len(data) == 1:
        break
print(sum(ans))