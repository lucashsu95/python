#608 最大最小值索引
ary = []
for i in range(9):
    ary.append(int(input()))
Lmax = max(ary)
LmaxIndex1 = ary.index(Lmax)//3
LmaxIndex2 = ary.index(Lmax)%3
Lmin = min(ary)
LminIndex1 = ary.index(Lmin)//3
LminIndex2 = ary.index(Lmin)%3
print(f'Index of the largest number {Lmax} is: ({LmaxIndex1}, {LmaxIndex2})')
print(f'Index of the smallest number {Lmin} is: ({LminIndex1}, {LminIndex2})')
