#TA001 漢明距離
a,b = list(map(int,input().split(' ')))
a = bin(a)
b = bin(b)

a = '{:>020s}'.format(str(a[2:]))
b = '{:>020s}'.format(str(b[2:]))
# print(a,b)
DifferentCount = 0
for i,j in zip(a,b):
    if i != j:
        DifferentCount += 1
print(a)
print(b)
print(DifferentCount)
