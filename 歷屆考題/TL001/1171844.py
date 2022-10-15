#TL001 把所有的數字改成英文
AtoZ = [chr(i) for i in range(97,123)]
data = list(input())
for i in range(len(data)):
    if data[i] not in AtoZ:
        data[i] = AtoZ[AtoZ.index(data[i-1]) + int(data[i])]
ans = ''.join(data)
print(ans)