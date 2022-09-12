#IMD2021 prob-獎牌
n = int(input())
Lmax = 0
ans = ''
for _ in range(n):
    data = input().split()
    Lsum = (int(data[0]) * 1000000) + (int(data[1]) * 1000) + int(data[2])
    name = ' '.join(data[3:])
    if Lsum > Lmax:
        Lmax = Lsum
        ans = name
print(ans)