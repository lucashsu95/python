#TL001 最大值及次大值的乘積
data = sorted(list(map(int,input().split())))
print((data[-1] - 1) * (data[-2] - 1))