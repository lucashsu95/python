#709 詞典排序
Lkey = input()
Ldict = {}
while Lkey != 'end':
    Lvalue = input()
    Ldict[Lkey] = Lvalue
    Lkey = input()
Ldict2 = sorted(Ldict)
for i in Ldict2:
    print(f'{i}: {Ldict[i]}')
