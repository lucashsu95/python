#詞典搜尋
Ldict = {}
Lkey = input()
while Lkey != 'end':
    Lvalue = input()
    Ldict[Lkey] = Lvalue
    Lkey = input()
print(Ldict)
Lsearch = input()
print(Lsearch in Ldict.keys())
    