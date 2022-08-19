#IMD2021 prob-獎牌
n = int(input())
ans = []
ansname = []
for _ in range(n):
    line = input().split()
    g = int(line[0])
    s = int(line[1])
    b = int(line[2])
    name = []

    for i in range(3,len(line)):
        name.append(line[i])
    name = ' '.join(name)
    Lsum = (g * 1000000) + (s * 1000) + b
    ans.append(Lsum)
    ansname.append(name)

print(ansname[ans.index(max(ans))])