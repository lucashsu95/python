#TL001 找出最高高度
data = input().split()
start = 0
Lmax = 0
for i in data:
    start += int(i)
    if start > Lmax : Lmax = start
print(Lmax)
