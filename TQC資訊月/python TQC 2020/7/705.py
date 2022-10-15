#705 子集合與超集合
Lset,Lset2,Lset3 = set(),set(),set()

for i in range(5):Lset.add(int(input()))
for i in range(3):Lset2.add(int(input()))
for i in range(9):Lset3.add(int(input()))
print('set2 is subset of set1:', Lset2.issubset(Lset))
print('set3 is superset of set1:', Lset3.issuperset(Lset))