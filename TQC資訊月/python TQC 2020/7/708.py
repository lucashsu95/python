#708 詞典合併
def compute():
    Ldict = {}
    Key = input()
    while Key != 'end':
        Value = input()
        Ldict[Key] = Value
        Key = input()
    return Ldict
print('Create dict1:')
print('Create dict2:')
Ldict = compute()
Ldict2 = compute()
Ldict.update(Ldict2)
Ldict3 = sorted(Ldict)
for i in Ldict3:
    print(f'{i}: {Ldict[i]}')