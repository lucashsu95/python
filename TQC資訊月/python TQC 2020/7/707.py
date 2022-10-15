#707 共同科目
Lset,Lset2 = set(),set()
Lstr = ['Enter group X’s subjects:','Enter group Y’s subjects:']
for i in range(2):
    print(Lstr[i])
    data = input()
    while data != 'end':
        if i == 0:
            Lset.add(data)
        else:
            Lset2.add(data)
        data = input()

Lset = set(sorted(Lset))
Lset2 = set(sorted(Lset2))
print(sorted(Lset | Lset2))
print(sorted(Lset & Lset2))
print(sorted(Lset2 - Lset))
print(sorted(Lset ^ Lset2))

