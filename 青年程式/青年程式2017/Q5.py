#題目 5：編碼(Coding)問題 (10%)
data = input()
Lans = ''
Lvalue = 0
Llist = list(data.lower())
Lset = sorted(set(data.lower()))

for i in range(len(Lset)):
    Lvalue += Llist.count(Lset[i])
    Lans += data[Lvalue-1] + str(Llist.count(Lset[i]))
print(''.join(Lans))